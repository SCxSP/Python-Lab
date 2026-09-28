import os, sys, subprocess, glob

SAMPLE_INPUTS = {
    # Assi1
    'Assi1/q1.py': ['Hello, World!'],
    'Assi1/q2.py': ['John'],
    'Assi1/q3.py': ['15', '4'],
    'Assi1/q4.py': ['7'],
    'Assi1/q5.py': ['10', '5'],
    'Assi1/q6.py': ['37'],
    'Assi1/q7.py': ['hello', '42'],
    'Assi1/q8.py': ['123'],
    'Assi1/q9.py': ['10 20 30'],
    'Assi1/q10.py': ['Alice', '80 85 90'],
    'Assi1/q11.py': ['10 20 30 40 50'],
    'Assi1/q12.py': ['10 20 30 40 50'],
    'Assi1/q13.py': ['1 2 3 4 5', '6'],
    'Assi1/q14.py': ['10 20 30 40 50', '30'],
    'Assi1/q15.py': ['1 2 3 4 5'],
    'Assi1/q16.py': ['Python'],
    'Assi1/q17.py': ['10 20 30 40 50'],
    'Assi1/q18.py': ['10 20 30 40 50', '2'],

    # Assi2
    'Assi2/q1.py': ['Hello World'],
    'Assi2/q2.py': ['Good ', 'Morning'],
    'Assi2/q3.py': ['Python Programming'],
    'Assi2/q4.py': ['Mississippi', 's'],
    'Assi2/q5.py': ['I love apples', 'apples', 'oranges'],
    'Assi2/q6.py': ['John', '20'],
    'Assi2/q7.py': ['John', 'Doe'],
    'Assi2/q8.py': ['10 50 20 40 30'],
    'Assi2/q9.py': ['10 20 30 40 50'],
    'Assi2/q10.py': ['1 2 3 4', '5'],
    'Assi2/q11.py': ['1 2 4 5', '2', '3'],
    'Assi2/q12.py': ['10 20 30 40', '30'],
    'Assi2/q13.py': ['10 20 30 40 50'],
    'Assi2/q14.py': ['50 20 10 40 30'],
    'Assi2/q15.py': ['10 50 20 40 30'],
    'Assi2/q16.py': ['M I S S I S S I P I', 'S'],
    'Assi2/q17.py': ['a b c d e', 'c'],
    'Assi2/q18.py': ['1 2 3 4 5'],
    'Assi2/q19.py': ['Alice', '101', '92'],
    'Assi2/q20.py': ['Bob', '80 85 90'],
    'Assi2/q21.py': ['1 2 3', '4 5 6', '7 8 9'],
    'Assi2/q22.py': ['80 85 90', '75 80 85', '90 92 95'],
    'Assi2/q23.py': ['1 2 3', '4 5 6', '1', '2'],
    'Assi2/q24.py': ['Alice', '80 85 90', 'Bob', '75 80 85', 'Charlie', '90 92 95'],
    'Assi2/q25.py': ['1 2 3', '4 5 6'],
    'Assi2/q26.py': ['10 50 30', '40 20 60'],
    'Assi2/q27.py': ['1 2 3', '4 5 6'],
    'Assi2/q28.py': ['Alice', '101', '80 85 90', 'Bob', '102', '75 80 85', 'Charlie', '103', '90 92 95'],

    # Assi3
    'Assi3/q1.py': ['75 80 85 90 95 60 65 70 88 92'],
    'Assi3/q2.py': ['Juice', 'Milk'],
    'Assi3/q3.py': ['30 32 35 31 29 28 33'],
    'Assi3/q4.py': ['101 102 101 103 102 104'],
    'Assi3/q5.py': ['1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20'],
    'Assi3/q6.py': ['2', 'Alice', '80 85 90', 'Bob', '75 80 85'],
    'Assi3/q7.py': ['10 50 20 40 30'],
    'Assi3/q8.py': ['10 20 30 40'],
    'Assi3/q9.py': ['Alice', '101', 'BCA', '92'],
    'Assi3/q10.py': ['0 0', '3 4'],
    'Assi3/q11.py': ['EMP101', 'John', 'IT', '75000'],
    'Assi3/q12.py': ['1 2 3 4 5 6 7 8 9 10 11 12 13 14 15', '7'],
    'Assi3/q13.py': ['75 80 85 90 95 60 65 70 88 92'],
    'Assi3/q14.py': ['Book1', 'Author1', '250', 'Book2', 'Author2', '300', 'Book3', 'Author3', '350', 'Book4', 'Author4', '400', 'Book5', 'Author5', '450'],
    'Assi3/q15.py': ['3', 'Alice', '85', 'Bob', '92', 'Charlie', '78'],
    'Assi3/q16.py': ['Alice', '9876543210', 'Bob', '9876543211', 'Charlie', '9876543212', 'David', '9876543213', 'Eva', '9876543214', 'Bob'],
    'Assi3/q17.py': ['2', 'apple', '10', 'banana', '20', 'orange', '15', 'apple', '12', 'banana'],
    'Assi3/q18.py': ['the quick brown fox jumps over the lazy dog'],
    'Assi3/q19.py': ['hello world'],
    'Assi3/q20.py': ['3', 'Alice', '60000', 'Bob', '45000', 'Charlie', '75000'],
    'Assi3/q21.py': ['Alice', '85', '90', '88', '92'],
    'Assi3/q22.py': ['3', 'Alice', '82', 'Bob', '65', 'Charlie', '38'],

    # Assi4
    'Assi4/q1.py': ['150'],
    'Assi4/q2.py': ['25'],
    'Assi4/q3.py': ['5000', '1200'],
    'Assi4/q4.py': ['8'],
    'Assi4/q5.py': ['82.5'],
    'Assi4/q6.py': ['6000', '7500', '8000', '5500', '9000', '6500', '7000'],
    'Assi4/q7.py': ['P', 'P', 'A', 'P', 'P', 'A', 'P', 'P', 'P', 'A'],
    'Assi4/q8.py': ['50', '100', '75', '120', '60', '80', '150', '90', '110', '130'],
    'Assi4/q9.py': ['1', '-2', '0', '4', '-5', '6', '0', '-8', '9', '10', '11', '-12', '13', '-14', '0', '16', '-17', '18', '19', '-20'],
    'Assi4/q10.py': ['Tea', 'Coffee', 'Tea', 'Juice', 'Tea', 'Coffee', 'Burger', 'Tea', 'Pizza', 'Burger', 'Coffee', 'Tea', 'Sandwich', 'Pizza', 'Tea'],
    'Assi4/q11.py': ['3', '5', '7'],
    'Assi4/q12.py': ['0000', '1234'],
    'Assi4/q13.py': ['1', '4'],
    'Assi4/q14.py': ['Alice', '101', 'y', 'Bob', '102', 'n'],
    'Assi4/q15.py': ['1000', '2000', '1500', '3000', '1000', '500', '2000', '2500', '1500'],
    'Assi4/q16.py': ['apple', '2', 'milk', '1', 'checkout'],
    'Assi4/q17.py': ['30', '45', '20', '60', '40', '50', '35'],
    'Assi4/q18.py': ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8', 'Book9', 'Book10'],
    'Assi4/q19.py': ['Apple', 'Banana', 'Mango', 'Orange', 'Grape'],
    'Assi4/q20.py': ['8', '7', '9', '8', '6', '8', '10'],
    'Assi4/q21.py': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah'],

    # Assi5
    'Assi5/q1.py': ['John'],
    'Assi5/q2.py': ['Alice', 'BCA', 'IEM'],
    'Assi5/q3.py': ['12', '4'],
    'Assi5/q4.py': ['5'],
    'Assi5/q5.py': ['7'],
    'Assi5/q6.py': ['10', '5'],
    'Assi5/q7.py': ['15', '3'],
    'Assi5/q8.py': ['Alice', '85 90 88'],
    'Assi5/q9.py': ['John', '20', 'BCA'],
    'Assi5/q10.py': ['Alice', 'IT', '85000'],
    'Assi5/q11.py': ['3', '4'],
    'Assi5/q12.py': ['8'],
    'Assi5/q13.py': ['9'],
    'Assi5/q14.py': ['15', '25'],
    'Assi5/q15.py': ['-5'],
    'Assi5/q16.py': ['1 2 3 4 5 6 7 8 9 10'],
    'Assi5/q17.py': ['10 20 30 40 50', '1 2 3 4 5'],
    'Assi5/q18.py': ['10 15 20 25 30 35 40 45 50'],
    'Assi5/q19.py': ['2 3 4 5 6 7 8 9 10 11 13 15 17 20'],
    'Assi5/q20.py': ['10 20 30 40 50'],
    'Assi5/q21.py': ['10'],
    'Assi5/q22.py': ['10 20 30 40 50'],
    'Assi5/q23.py': ['5'],
    'Assi5/q24.py': ['6'],
    'Assi5/q25.py': ['50'],

    # Assi6
    'Assi6/q1.py': ['5'],
    'Assi6/q2.py': ['7'],
    'Assi6/q3.py': ['10'],
    'Assi6/q4.py': ['12345'],
    'Assi6/q5.py': ['Hello Closure'],
    'Assi6/q6.py': ['3', '2'],
    'Assi6/q7.py': ['4'],
    'Assi6/q8.py': ['Alice'],
    'Assi6/q9.py': ['1000'],
    'Assi6/q10.py': ['5', '10'],
    'Assi6/q11.py': ['Alice', '101', '88', 'Bob', '102', '92', 'Charlie', '103', '79'],
    'Assi6/q12.py': ['Alice', '75000', 'Bob', '82000'],
    'Assi6/q13.py': ['8', '5'],
    'Assi6/q14.py': ['10000', '5.5'],
    'Assi6/q15.py': ['Python Crash Course', 'Eric Matthes', '550'],
    'Assi6/q16.py': ['TestObject'],
    'Assi6/q17.py': ['Alice', '20', '101', 'BCA'],
    'Assi6/q18.py': ['Tesla'],
    'Assi6/q19.py': ['Alex'],
    'Assi6/q20.py': ['10', '20', '30'],
    'Assi6/q21.py': ['2 3', '4 5'],
    'Assi6/q22.py': ['dog'],
    'Assi6/q23.py': ['7', '10 5'],
    'Assi6/q24.py': ['John'],
    'Assi6/q25.py': ['DemoTag'],

    # Assi7
    'Assi7/q1.py': ['Alice', '101', '88', 'Bob', '102', '92', 'Charlie', '103', '79'],
    'Assi7/q2.py': ['Alice', 'E101', 'IT', '85000'],
    'Assi7/q3.py': ['Alice', '75000', 'Bob', '82000'],
    'Assi7/q4.py': ['12', '5'],
    'Assi7/q5.py': ['ACC101', '5000', '2000', '1000'],
    'Assi7/q6.py': ['Alice', '20', '101', 'BCA'],
    'Assi7/q7.py': ['Tesla'],
    'Assi7/q8.py': ['Alex'],
    'Assi7/q9.py': ['7', '10', '5', '6', '8'],
    'Assi7/q10.py': ['dog'],
    'Assi7/q11.py': ['5 8', '3 6'],
    'Assi7/q12.py': ['10', '20', '30'],
    'Assi7/q13.py': ['7', '10 5', '6 8'],
    'Assi7/q14.py': ['7', '10 5'],
    'Assi7/q15.py': ['DemoTag'],
    'Assi7/q16.py': ['10', '2'],
    'Assi7/q17.py': ['20', '4'],
    'Assi7/q18.py': ['9'],
    'Assi7/q19.py': ['21'],
    'Assi7/q20.py': ['15', '3', '/'],
    'Assi7/q21.py': ['Alice', '101', 'BCA', '92'],
    'Assi7/q22.py': ['student.txt'],
    'Assi7/q23.py': ['student.txt'],
    'Assi7/q24.py': ['student.txt', 'destination.txt'],
    'Assi7/q25.py': ['student.txt'],

    # Assi8
    'Assi8/q1.py': ['10 20 30 40 50 60 70 80 90 100'],
    'Assi8/q2.py': ['10 20 30 40 50 60 70 80 90 100'],
    'Assi8/q3.py': ['1 2 3 4 5 6 7 8 9 10', '2', '99', '100', '5'],
    'Assi8/q4.py': ['45 12 89 23 67 34 90 11 56 78'],
    'Assi8/q5.py': ['10 20 30 40 50 30 60 30 70 80', '30'],
    'Assi8/q6.py': ['5'],
    'Assi8/q7.py': ['3'],
    'Assi8/q8.py': ['1 2 3 4', '5 6 7 8'],
    'Assi8/q9.py': ['75 80 85 90 95 60 65 70 88 92'],
    'Assi8/q10.py': [],
    'Assi8/q11.py': ['1 2 3 4 5 6 7 8 9', '9 8 7 6 5 4 3 2 1'],
    'Assi8/q12.py': ['10 25 30 45 50 55 60 75 80 15 20 35 40 65 70 85 90 95 5 100'],
    'Assi8/q13.py': ['0 30 45 60 90'],
    'Assi8/q14.py': ['1 2 3 4', '5 6 7 8'],
    'Assi8/q15.py': [],
    'Assi8/q16.py': ['75 80 85 90 95 60 65 70 88 92'],
    'Assi8/q17.py': ['103'],
    'Assi8/q18.py': ['CS'],
    'Assi8/q19.py': [],
    'Assi8/q20.py': [],
    'Assi8/q21.py': [],
    'Assi8/q22.py': [],
    'Assi8/q23.py': [],
    'Assi8/q24.py': [],
    'Assi8/q25.py': [],

    # Assi9
    'Assi9/q1.py': [],
    'Assi9/q2.py': [],
    'Assi9/q3.py': [],
    'Assi9/q4.py': [],
    'Assi9/q5.py': [],
    'Assi9/q6.py': [],
    'Assi9/q7.py': [],
    'Assi9/q8.py': [],
    'Assi9/q9.py': [],
    'Assi9/q10.py': [],
    'Assi9/q11.py': [],
    'Assi9/q12.py': [],
    'Assi9/q13.py': [],
    'Assi9/q14.py': [],
    'Assi9/q15.py': [],
    'Assi9/q16.py': [],
    'Assi9/q17.py': [],
    'Assi9/q18.py': [],
    'Assi9/q19.py': [],
    'Assi9/q20.py': [],
    'Assi9/q21.py': [],
    'Assi9/q22.py': [],
    'Assi9/q23.py': [],

    # Assi10
    'Assi10/q1.py': [],
    'Assi10/q2.py': [],
    'Assi10/q3.py': ['A', 'G'],
    'Assi10/q4.py': [],
    'Assi10/q5.py': [],
    'Assi10/q6.py': ['Arad'],
    'Assi10/q7.py': ['gets_grade_A'],
    'Assi10/q8.py': ['Car'],
    'Assi10/q9.py': ['vacuum'],
    'Assi10/q10.py': []
}

def normalize_path(path):
    return path.replace('\\', '/')

def run_program(file_path):
    norm_path = normalize_path(file_path)
    sample_list = SAMPLE_INPUTS.get(norm_path, [])
    
    script_runner = f'''
import os, sys, builtins
os.environ["MPLBACKEND"] = "Agg"

inputs = {repr(sample_list)}
input_iter = iter(inputs)

def custom_input(prompt=""):
    sys.stdout.write(str(prompt))
    sys.stdout.flush()
    try:
        val = next(input_iter)
    except StopIteration:
        val = ""
    sys.stdout.write(str(val) + "\\n")
    sys.stdout.flush()
    return val

builtins.input = custom_input

try:
    import tkinter as tk
    tk.Tk.mainloop = lambda self: self.after(50, self.destroy())
except Exception:
    pass

with open(r"{file_path}", "r", encoding="utf-8") as f:
    exec(compile(f.read(), r"{file_path}", "exec"))
'''
    try:
        proc = subprocess.run(
            [sys.executable, '-c', script_runner],
            text=True,
            capture_output=True,
            timeout=10
        )
        return proc.stdout.strip()
    except Exception:
        return ""

def run_assignment(lab_num):
    folder = f'Assi{lab_num}'
    files = sorted(glob.glob(f'{folder}/*.py'), key=lambda x: int(''.join(filter(str.isdigit, x)) or 0))
    for f in files:
        f_norm = normalize_path(f)
        out = run_program(f)
        print(f"--- {f_norm} ---")
        if out:
            print(out)
        print()

if __name__ == '__main__':
    target = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if target.lower() == 'all':
        for lab in range(1, 11):
            run_assignment(lab)
    else:
        lab_no = int(''.join(filter(str.isdigit, target)) or target)
        run_assignment(lab_no)
