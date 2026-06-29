#!/bin/bash

set -e

echo "========================================="
echo "Removing RSync Monitoring Service.."
echo "========================================="

# Set Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# Stop & Remove Service
sudo systemctl stop nve-rsync-monitor
sudo systemctl reset-failed nve-rsync-monitor
sudo systemctl disable nve-rsync-monitor
sudo rm /etc/systemd/system/nve-rsync-monitor.service
sudo systemctl daemon-reload
#sudo systemctl mask nve-rsync-monitor.service # !DANGER: disabled

# Deactivate Pyton venv
#deactivate

# Remove Project files
cd ..
rm -rf $PROJECT_DIR

# Check Project Directory
ls -1X /opt/apps

# Print Final Message
echo "========================================="
echo "DONE!"
echo "========================================="
