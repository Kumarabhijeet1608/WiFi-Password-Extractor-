#!/usr/bin/env python3
"""
Build Script for Network Security Tool v2.0
Author: Kumar
Automates the compilation process with enhanced error handling
"""

import os
import sys
import subprocess
import shutil
import time
import random
import string

def print_banner():
    """Print the build banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    🔐 Network Security Tool v2.0            ║
    ║                    Enhanced Build Script                    ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)

def check_dependencies():
    """Check if required dependencies are installed"""
    print("🔍 Checking dependencies...")
    
    required_packages = [
        "requests", "psutil", "cx_Freeze", "cryptography"
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} - MISSING")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Install them using: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True

def clean_build_directory():
    """Clean previous build artifacts"""
    print("\n🧹 Cleaning build directory...")
    
    build_dirs = ["build", "dist", "__pycache__"]
    
    for dir_name in build_dirs:
        if os.path.exists(dir_name):
            try:
                shutil.rmtree(dir_name)
                print(f"  ✅ Removed {dir_name}")
            except Exception as e:
                print(f"  ⚠️  Could not remove {dir_name}: {e}")
    
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".pyc"):
                try:
                    os.remove(os.path.join(root, file))
                except:
                    pass

def generate_random_build_id():
    """Generate random build identifier"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(16))

def build_executable():
    """Build the executable using setup.py"""
    print("\n🔨 Building executable...")
    
    try:
        result = subprocess.run(
            [sys.executable, "setup.py", "build"],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            print("✅ Build completed successfully!")
            return True
        else:
            print(f"❌ Build failed with error code: {result.returncode}")
            print(f"Error output: {result.stderr}")
            return False
            
    except subprocess.TimeoutExpired:
        print("❌ Build timed out after 5 minutes")
        return False
    except Exception as e:
        print(f"❌ Build error: {e}")
        return False

def verify_build():
    """Verify the build output"""
    print("\n🔍 Verifying build output...")
    
    build_dir = "build"
    if not os.path.exists(build_dir):
        print("❌ Build directory not found")
        return False
    
    exe_found = False
    for root, dirs, files in os.walk(build_dir):
        for file in files:
            if file.endswith(".exe") or file.endswith(""):
                exe_path = os.path.join(root, file)
                exe_size = os.path.getsize(exe_path)
                print(f"  ✅ Found executable: {file}")
                print(f"      Size: {exe_size / 1024 / 1024:.2f} MB")
                print(f"      Path: {exe_path}")
                exe_found = True
                break
    
    if not exe_found:
        print("❌ No executable found in build output")
        return False
    
    return True

def create_deployment_package():
    """Create a deployment package"""
    print("\n📦 Creating deployment package...")
    
    try:
        deploy_dir = "deployment"
        if os.path.exists(deploy_dir):
            shutil.rmtree(deploy_dir)
        
        os.makedirs(deploy_dir)
        
        build_dir = "build"
        if os.path.exists(build_dir):
            for item in os.listdir(build_dir):
                src = os.path.join(build_dir, item)
                dst = os.path.join(deploy_dir, item)
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
        
        deploy_readme = f"""# Network Security Tool v2.0 - Deployment Package

Build ID: {generate_random_build_id()}
Build Date: {time.strftime('%Y-%m-%d %H:%M:%S')}
Version: 2.0.1
Author: Kumar

## Instructions:
1. Extract this package
2. Run the executable on the target system
3. Network analysis data will be sent to configured channel
4. Tool will clean up after execution

## Features:
- Enhanced security analysis
- Discord integration
- Cross-platform support
- Automatic cleanup

⚠️  Use responsibly and only on authorized systems!
"""
        
        with open(os.path.join(deploy_dir, "README.txt"), "w") as f:
            f.write(deploy_readme)
        
        print(f"✅ Deployment package created: {deploy_dir}/")
        return True
        
    except Exception as e:
        print(f"❌ Failed to create deployment package: {e}")
        return False

def main():
    """Main build process"""
    print_banner()
    
    if not check_dependencies():
        print("\n❌ Cannot proceed without dependencies")
        sys.exit(1)
    
    clean_build_directory()
    
    if not build_executable():
        print("\n❌ Build failed")
        sys.exit(1)
    
    if not verify_build():
        print("\n❌ Build verification failed")
        sys.exit(1)
    
    if not create_deployment_package():
        print("\n⚠️  Deployment package creation failed")
    
    print("\n🎉 Build process completed successfully!")
    print("\n📁 Output files:")
    print("  - build/          - Build artifacts")
    print("  - deployment/     - Ready-to-deploy package")
    print("\n📋 Next steps:")
    print("  1. Test the executable in a safe environment")
    print("  2. Deploy to target system")
    print("  3. Monitor configured channel for data")
    print("\n⚠️  Remember: Use responsibly and legally!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Build interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
