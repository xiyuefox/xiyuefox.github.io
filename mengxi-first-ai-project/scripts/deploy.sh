#!/bin/bash

# Redirect to the new Unified Workflow Script
# This ensures the existing Automator App works with the new system.

SCRIPT_DIR=$(dirname "$0")
"$SCRIPT_DIR/sync-and-publish.sh"


echo "✅ Deployment Complete! Your blog is updated."
