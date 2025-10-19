import base64
import os
import sys
import tempfile

def build_executable(encoded_script):
    # Decode the script
    script_content = base64.b64decode(encoded_script).decode('utf-8')
    
    # Create obfuscated version
    obfuscated_script = obfuscate_code(script_content)
    
    # Write to temporary file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
        f.write(obfuscated_script)
        temp_script = f.name
    
    # Build with PyInstaller
    os.system(f'pyinstaller --onefile --noconsole {temp_script}')
    
    # Cleanup
    os.unlink(temp_script)

def obfuscate_code(script):
    # Add basic obfuscation techniques
    obfuscated = f'''
import base64
import sys
import types

# Obfuscated payload
encoded_payload = "{base64.b64encode(script.encode()).decode()}"

# Decode and execute
decoded = base64.b64decode(encoded_payload).decode()
exec(decoded)
'''
    return obfuscated

if __name__ == "__main__":
    if len(sys.argv) > 1:
        build_executable(sys.argv[1])
