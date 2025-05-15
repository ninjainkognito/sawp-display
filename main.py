import sys
import re
import os

def correctMainDisplay(displayplacer_string: str):
    """
    Processes the display configuration string by swapping the origin values between display configurations,
    and executes the swapped command before the initial command.
    
    :param displayplacer_string: String related to display settings.
    """
    print("🔄 Start Skript correctMainDisplay()")

    try:
        def swap_origins(display_string):
            # Match the origin values with a regular expression
            origins = re.findall(r'origin:\(\d+,\d+\)', display_string)
            
            # Ensure that exactly two origin values are found
            if len(origins) != 2:
                raise ValueError("Invalid number of origin values.")
            
            # Swap the origin values
            swapped_string = display_string.replace(origins[0], 'placeholder').replace(origins[1], origins[0]).replace('placeholder', origins[1])
            
            return swapped_string
        
        # Split the displayplacer output into lines
        lines = displayplacer_string.splitlines()
        
        # Get the last line of the output
        last_line = lines[-1] if lines else None
        
        # Store the last line in a variable
        command_to_set_current_screens = last_line
        
        # Swap the origin values
        swapped_display_string = swap_origins(command_to_set_current_screens)
        
        # Execute the swapped command
        # print("Executing the swapped display setup command...")
        os.system(swapped_display_string)

        # Execute the initial command
        # print("Executing the initial display setup command...")
        os.system(command_to_set_current_screens)

        print(f"✅ Processing successful! Swapped and initial commands executed.")

    except Exception as e:
        print(f"❌ Error during processing: {e}")

    finally:
        print("⏹️  Ende Skript correctMainDisplay()")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python main.py <displayplacer list>")
    else:
        displayplacer_string = sys.argv[1]
        correctMainDisplay(displayplacer_string)
