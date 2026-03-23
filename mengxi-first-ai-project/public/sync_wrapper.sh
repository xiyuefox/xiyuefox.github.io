#!/bin/zsh
# Node, Python and API keys wrapper for launchd

# 1. Load User Profile Environment
if [ -f "$HOME/.zshrc" ]; then
    source "$HOME/.zshrc"
elif [ -f "$HOME/.bash_profile" ]; then
    source "$HOME/.bash_profile"
fi

# 2. Change Directory to Project Root
cd "/Users/hulimofaqiu/mengxi-first-ai-project"

# 3. Ensure logs directory exists
mkdir -p logs

# 4. Run sync.sh
./sync.sh
