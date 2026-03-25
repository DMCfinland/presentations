# API Key Security Guide

## ✅ Safe Practices

### Option 1: Environment Variable (Recommended for local use)
```bash
# Add to your ~/.zshrc or ~/.bashrc (never commit this file)
export ANTHROPIC_API_KEY="sk-ant-your-key-here"

# Reload shell
source ~/.zshrc

# Test it works
echo $ANTHROPIC_API_KEY
```

### Option 2: .env File (Good for projects)
```bash
# 1. Copy the example
cp .env.example .env

# 2. Edit .env and add your real key
# ANTHROPIC_API_KEY=sk-ant-your-key-here

# 3. The .env file is gitignored automatically (NEVER commit it!)
```

Then use with python-dotenv:
```python
from dotenv import load_dotenv
load_dotenv()
# Now os.environ['ANTHROPIC_API_KEY'] is available
```

### Option 3: Pass directly (Least secure, only for testing)
```python
client = anthropic.Anthropic(api_key="sk-ant-...")
# Don't use this in production!
```

## ❌ NEVER Do These

1. ❌ Commit API keys to Git
2. ❌ Share keys in screenshots or videos
3. ❌ Hardcode keys in scripts that get committed
4. ❌ Store keys in shared Dropbox/OneDrive folders
5. ❌ Email or Slack your keys

## 🔍 Check for Leaked Keys

```bash
# Search for potential leaks in your codebase
git grep -i "sk-ant-"
git grep -i "api_key"
```

## 🚨 If You Leaked a Key

1. Go to https://console.anthropic.com/settings/keys
2. Delete the compromised key immediately
3. Generate a new key
4. Update your .env or environment variable

## 📦 For Production

Consider using:
- **1Password** / **Bitwarden**: Store keys in password manager
- **AWS Secrets Manager**: For cloud deployments
- **Doppler**: Environment variable management service
- **GitHub Secrets**: For CI/CD workflows
