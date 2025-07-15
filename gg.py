import matplotlib.pyplot as plt

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
    first_half=-1
    second_half=1
    prev='';
    for i, bit in enumerate(data):
        if bit == '1' and prev=='1'  or bit == '1' and prev=='0' :
            # '1' = low to high
            first_half = first_half*(-1)
            second_half =second_half *( -1)
            prev=bit;
        else:
            # '0' = high to low
            first_half = first_half
            second_half = second_half
            prev=bit;
        signal.extend([first_half, second_half, second_half])
        time.extend([i, i + 0.5, i + 1])
    return time, signal
    
def rz_encoding(data):
    """RZ encoding with mid-bit transitions"""
    signal = []
    time = []
    for i, bit in enumerate(data):
        if bit == '1':
            signal.extend([1, 0, 0])
        else:
            signal.extend([-1, 0, 0])
        time.extend([i, i + 0.5, i + 1])
    return time, signal

# Input digital data
digital_data = "10110"

# Get time and signal for all encodings
t1, s1 = nrzl_encoding(digital_data)
t2, s2 = nrzi_encoding(digital_data)
t3, s3 = manchester_encoding(digital_data)
t4, s4 = diff_manchester_encoding(digital_data)
t5, s5 = rz_encoding(digital_data)
# Track positions (visual levels on the plot)
track_gap = 3
s1 = [y + track_gap * 4 for y in s1]  # NRZ-L at top
s2 = [y + track_gap * 3 for y in s2]  # NRZ-I
s3 = [y + track_gap * 2 for y in s3]  # Manchester
s4 = [y + track_gap * 1 for y in s4]  # Differential Manchester
s5 = [y + track_gap * 0 for y in s5]  # RZ at bottom
# Plot
plt.figure(figsize=(14, 16))
plt.plot(t1, s1, drawstyle='steps-post', label="NRZ-L", color='blue')
plt.plot(t2, s2, drawstyle='steps-post', label="NRZ-I", color='red')
plt.plot(t3, s3, drawstyle='steps-post', label="Manchester", color='green')
plt.plot(t4, s4, drawstyle='steps-post', label="Diff Manchester", color='purple')
plt.plot(t5, s5, drawstyle='steps-post', label="RZ", color='orange')

# Add track labels
plt.yticks(
    [track_gap * 4,track_gap * 3, track_gap * 2, track_gap * 1, 0],
    ["NRZ-L", "NRZ-I", "Manchester", "Diff Manchester","RZ"]
)

for i, bit in enumerate(digital_data):
    plt.text(i + 0.5, max(s1) + 0.5, bit, ha='center', va='bottom', fontsize=12, fontweight='bold')

# plt.title("Digital Data to Digital Signal (All 4 Encodings)",fontsize=15)
plt.xlabel("Time")
plt.ylabel("Voltage Level (Shared Grid)")
plt.grid(True)
plt.grid(axis='x', color='black', linestyle='--', linewidth=1.2)
plt.grid(axis='y',  linewidth=1.5)
# plt.subplots_adjust(top=0.7) 
# plt.legend(loc='lower right')
plt.tight_layout()
plt.show()