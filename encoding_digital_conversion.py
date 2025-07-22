import matplotlib.pyplot as plt

# ---------- Encoding Functions ----------

def unipolar_nrz_encoding(data):
    signal, time = [], []
    for i, bit in enumerate(data):
        level = 1 if bit == '1' else 0
        signal.extend([level, level])
        time.extend([i, i + 1])
    return time, signal

def nrzl_encoding(data):
    signal, time = [], []
    for i, bit in enumerate(data):
        level = 1 if bit == '1' else -1
        signal.extend([level, level])
        time.extend([i, i + 1])
    return time, signal

def nrzi_encoding(data):
    signal, time = [], []
    current_level = 1
    for i, bit in enumerate(data):
        if bit == '1':
            current_level *= -1
        signal.extend([current_level, current_level])
        time.extend([i, i + 1])
    return time, signal

def manchester_encoding(data):
    signal, time = [], []
    for i, bit in enumerate(data):
        first = -1 if bit == '1' else 1
        second = 1 if bit == '1' else -1
        signal.extend([first, second, second])
        time.extend([i, i + 0.5, i + 1])
    return time, signal

def diff_manchester_encoding(data):
    signal, time = [], []
    last = -1
    for i, bit in enumerate(data):
        if bit == '0':
            last *= -1  # Start transition for 0
        signal.extend([last, -last, -last])
        time.extend([i, i + 0.5, i + 1])
    return time, signal

def rz_encoding(data):
    signal, time = [], []
    for i, bit in enumerate(data):
        if bit == '1':
            signal.extend([1, 0, 0])
        else:
            signal.extend([-1, 0, 0])
        time.extend([i, i + 0.5, i + 1])
    return time, signal

def ami_encoding(data):
    signal, time = [], []
    last = -1
    for i, bit in enumerate(data):
        if bit == '0':
            signal.extend([0, 0])
        else:
            last *= -1
            signal.extend([last, last])
        time.extend([i, i + 1])
    return time, signal

def pseudoternary_encoding(data):
    signal, time = [], []
    last = -1
    for i, bit in enumerate(data):
        if bit == '1':
            signal.extend([0, 0])
        else:
            last *= -1
            signal.extend([last, last])
        time.extend([i, i + 1])
    return time, signal

# ---------- Input Data ----------
digital_data = "1011010011"

# ---------- Generate All Encodings ----------
t0, s0 = unipolar_nrz_encoding(digital_data)
t1, s1 = nrzl_encoding(digital_data)
t2, s2 = nrzi_encoding(digital_data)
t3, s3 = manchester_encoding(digital_data)
t4, s4 = diff_manchester_encoding(digital_data)
t5, s5 = rz_encoding(digital_data)
t6, s6 = ami_encoding(digital_data)
t7, s7 = pseudoternary_encoding(digital_data)

# ---------- Vertical Placement ----------
track_gap = 3
s0 = [y + track_gap * 7 for y in s0]  # Unipolar NRZ
s1 = [y + track_gap * 6 for y in s1]  # NRZ-L
s2 = [y + track_gap * 5 for y in s2]  # NRZ-I
s3 = [y + track_gap * 4 for y in s3]  # Manchester
s4 = [y + track_gap * 3 for y in s4]  # Diff Manchester
s5 = [y + track_gap * 2 for y in s5]  # RZ
s6 = [y + track_gap * 1 for y in s6]  # AMI
s7 = [y + track_gap * 0 for y in s7]  # Pseudoternary

# ---------- Plot ----------
plt.figure(figsize=(14, 22))
plt.plot(t0, s0, drawstyle='steps-post', label="Unipolar NRZ", color='darkcyan')
plt.plot(t1, s1, drawstyle='steps-post', label="NRZ-L", color='blue')
plt.plot(t2, s2, drawstyle='steps-post', label="NRZ-I", color='red')
plt.plot(t3, s3, drawstyle='steps-post', label="Manchester", color='green')
plt.plot(t4, s4, drawstyle='steps-post', label="Diff Manchester", color='purple')
plt.plot(t5, s5, drawstyle='steps-post', label="RZ", color='orange')
plt.plot(t6, s6, drawstyle='steps-post', label="AMI", color='brown')
plt.plot(t7, s7, drawstyle='steps-post', label="Pseudoternary", color='magenta')

# ---------- Y-axis Labels ----------
plt.yticks(
    [track_gap * i for i in range(8)],
    ["Pseudoternary", "AMI", "RZ", "Diff Manchester", "Manchester", "NRZ-I", "NRZ-L", "Unipolar NRZ"]
)

# ---------- Input Bit Labels ----------
for i, bit in enumerate(digital_data):
    plt.text(i + 0.5, max(s0) + 1, bit, ha='center', va='top', fontsize=12, fontweight='bold')

# ---------- Final Touch ----------
plt.xlabel("Time")
plt.ylabel("Voltage Level (Shared Grid)")
plt.grid(True)
plt.grid(axis='x', color='black', linestyle='--', linewidth=1.2)
plt.grid(axis='y', linewidth=1.5)
plt.tight_layout()
plt.show()



