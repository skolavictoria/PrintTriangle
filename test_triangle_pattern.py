import subprocess

# Function to compile and run the student's C program, then test the output.
def test_triangle_pattern():
    # Compile the C program
    compile_process = subprocess.run(['gcc', 'triangle_pattern.c', '-o', 'triangle_pattern'], capture_output=True, text=True, encoding='utf-8')
    if compile_process.returncode != 0:
        print("Compilation failed.")
        print(compile_process.stderr)
        return

    # Run the compiled program with input 5, assuming it takes input from stdin
    run_process = subprocess.run(['./triangle_pattern'], input='5', capture_output=True, text=True, stdin=subprocess.PIPE)
    if run_process.returncode != 0:
        print("Runtime error.")
        print(run_process.stderr)
        return

    # Assuming the program writes output to output.txt
    with open('output.txt', 'r') as file:
        output = file.read().strip()

    # Define the expected output for input 5
    expected_output = "@\n@@\n@@@\n@@@@\n@@@@@"

    # Check if the program's output matches the expected output
    assert output == expected_output, "The output did not match the expected output."
    print("Test passed. The triangle pattern is correct.")

if __name__ == "__main__":
    test_triangle_pattern()
