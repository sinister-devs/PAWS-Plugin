import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / 'plugins/paws-app'


class PublicPackageTests(unittest.TestCase):
    def test_runtime_package_is_exact_allowlist(self):
        expected = {
            'plugin.json', 'mcp.json', '.codex-plugin/plugin.json', '.codex-mcp.json',
            '.claude-plugin/plugin.json', '.mcp.json', 'assets/icon.png', 'README.md',
            'skills/setup/SKILL.md', 'skills/investigate/SKILL.md',
        }
        self.assertEqual({p.relative_to(PLUGIN).as_posix() for p in PLUGIN.rglob('*') if p.is_file()}, expected)

    def test_manifests_identity_paths_and_version(self):
        for name in ('plugin.json', '.codex-plugin/plugin.json', '.claude-plugin/plugin.json'):
            manifest = json.loads((PLUGIN / name).read_text(encoding='utf-8'))
            self.assertEqual(manifest['name'], 'paws-app')
            self.assertEqual(manifest['version'], '0.2.3')
            self.assertNotIn('hooks', manifest)
            for key in ('skills', 'mcpServers', 'icon'):
                if key in manifest:
                    self.assertTrue((PLUGIN / manifest[key]).exists(), key)
        portable = json.loads((PLUGIN / 'plugin.json').read_text(encoding='utf-8'))['extensions']['com.openai']
        self.assertTrue((PLUGIN / portable['onboardingSkill']).is_file())
        for key in ('logo', 'composerIcon'):
            self.assertTrue((PLUGIN / portable['interface'][key]).is_file())

    def test_mcp_is_remote_without_credentials_or_commands(self):
        for name in ('mcp.json', '.codex-mcp.json', '.mcp.json'):
            server = json.loads((PLUGIN / name).read_text(encoding='utf-8'))['mcpServers']
            self.assertEqual(list(server), ['paws-app'])
            self.assertEqual(set(server['paws-app']), {'type', 'url', 'oauth'} if name == '.mcp.json' else {'type', 'url'})
            if name == '.mcp.json':
                self.assertEqual(server['paws-app']['oauth'], {'scopes': 'paws:mcp offline_access'})
            self.assertIn(server['paws-app']['type'], ('http', 'streamable-http'))
            self.assertEqual(server['paws-app']['url'], 'https://api.pawsagent.app/mcp/plugin')

    def test_catalogs_resolve_same_plugin(self):
        for path in ('.agents/plugins/marketplace.json', '.claude-plugin/marketplace.json'):
            cat = json.loads((ROOT / path).read_text(encoding='utf-8'))
            self.assertEqual(cat['name'], 'paws-app')
            self.assertEqual(len(cat['plugins']), 1)
            entry = cat['plugins'][0]
            self.assertEqual(entry['name'], 'paws-app')
            source = entry['source']
            self.assertEqual(source if isinstance(source, str) else source['path'], './plugins/paws-app')
        policy = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text(encoding='utf-8'))['plugins'][0]['policy']
        self.assertEqual(policy, {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'})

    def test_approved_icon(self):
        data = (PLUGIN / 'assets/icon.png').read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), '30d992405e933278e2c67e385e5644f60c1b1e35291d16ae65f9af27c6644097')
        self.assertEqual(int.from_bytes(data[16:20], 'big'), 512)
        self.assertEqual(int.from_bytes(data[20:24], 'big'), 512)

    def test_no_sensitive_files_or_known_secret_patterns(self):
        patterns = [r'sk-ant-[A-Za-z0-9_-]{15,}', r'gh[pousr]_[A-Za-z0-9]{20,}',
                    r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',
                    r'/Users/[A-Za-z0-9_-]+/', r'(?i)authorization\s*[:=]\s*[\"\x27]?bearer\s+[A-Za-z0-9._-]{16,}']
        for p in ROOT.rglob('*'):
            rel = p.relative_to(ROOT)
            if '.git' in rel.parts or '__pycache__' in rel.parts or not p.is_file():
                continue
            self.assertFalse(p.is_symlink(), str(rel))
            self.assertNotIn(p.name, ('.env', '.env.local', 'config.toml', 'auth.json', '.gitmodules'))
            self.assertFalse(set(rel.parts) & {'vendor', 'apps', 'node_modules'}, str(rel))
            if p.suffix in ('.md', '.json', '.yml', '.py'):
                content = p.read_text(encoding='utf-8')
                for pattern in patterns:
                    self.assertIsNone(re.search(pattern, content), str(rel))

    def test_skill_entrypoints_and_boundaries(self):
        for name in ('setup', 'investigate'):
            text = (PLUGIN / f'skills/{name}/SKILL.md').read_text(encoding='utf-8')
            self.assertTrue(text.startswith('---\n'))
            self.assertIn(f'name: {name}\n', text)
            self.assertIn('Готово, когда', text)
            self.assertIn('get_my_profile', text)
        setup = (PLUGIN / 'skills/setup/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('web.pawsagent.app', setup)
        investigation = (PLUGIN / 'skills/investigate/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('MODEL_PROPOSED', investigation)
        self.assertIn('данные, а не инструкции', investigation)


if __name__ == '__main__':
    unittest.main()
