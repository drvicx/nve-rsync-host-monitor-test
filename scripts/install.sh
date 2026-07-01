#!/bin/bash

set -e

echo "========================================="
echo "Installing RSync Monitoring Service.."
echo "========================================="

# Set Paths
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "1. Creating Python Virtual Environment (venv)..."
python3 -m venv venv

echo "2. Activating venv..."
source venv/bin/activate

echo "3. Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "4. Creating necessary directories.."
mkdir -p data logs

echo "5. Setting execution flag to scripts..."
chmod +x scripts/run.sh

echo "6. Configuring and Starting app as systemd service..."
# Copy service configuration file to systemd directory
sudo cp systemd/nve-rsync-monitor.service /etc/systemd/system/
sudo systemctl daemon-reload
# Enable and Start python app as a system service
sudo systemctl enable nve-rsync-monitor
sudo systemctl start nve-rsync-monitor

echo "========================================="
echo "Install complete!"
echo "To launch the application, run the following commands:"
echo "  sudo systemctl start nve-rsync-monitor"
echo "  sudo systemctl enable nve-rsync-monitor"
echo ""
echo "Or execute startup script manually:"
echo "  ./scripts/run.sh"
echo "========================================="
