def sort_file_contents(input_file, output_file):
    try:
        # Read contents from the input file
        with open(input_file, 'r') as file:
            lines = file.readlines()
        
        # Sort the lines
        sorted_lines = sorted(lines)

        # Write sorted lines to the output file
        with open(output_file, 'w') as file:
            file.writelines(sorted_lines)

        print(f"Sorted contents written to {output_file}")
    
    except FileNotFoundError:
        print("Error: The input file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_filename = "input.txt"   # Replace with your input file name
output_filename = "sorted_output.txt"  # Replace with your desired output file name

sort_file_contents(input_filename, output_filename)