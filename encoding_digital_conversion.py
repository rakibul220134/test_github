import matplotlib.pyplot as plt

# ---------- Encoding Functions ----------

def unipolar_nrz(data):
    return [1 if bit == 1 else 0 for bit in data]

def polar_nrz(data):
    return [1 if bit == 1 else -1 for bit in data]

def nrzi(data):
    signal = []
    last = 1
    for bit in data:
        if bit == 1:
            last *= -1
        signal.append(last)
    return signal

def rz(data):
    signal = []
    for bit in data:
        if bit == 1:
            signal.extend([1, 0])
        else:
            signal.extend([-1, 0])
    return signal

def manchester(data):
    return [[-1, 1] if bit == 1 else [1, -1] for bit in data]

def diff_manchester(data):
    signal = []
    last = 1
    for bit in data:
        if bit == 0:
            last *= -1
        signal.append([last, -last])
    return signal

def ami(data):
    signal = []
    last = -1
    for bit in data:
        if bit == 0:
            signal.append(0)
        else:
            last *= -1
            signal.append(last)
    return signal

def bipolar_rz(data):
    signal = []
    last = -1
    for bit in data:
        if bit == 0:
            signal.append([0, 0])
        else:
            last *= -1
            signal.append([last, 0])
    return signal

# ---------- Plotting Function ----------

def plot_encoding(data, encoding_fn, title, bits_per_symbol=1, paired=False):
    # Get encoded signal
    if paired:
        encoded_pairs = encoding_fn(data)
        encoded = [val for pair in encoded_pairs for val in pair]
    else:
        encoded = encoding_fn(data)

    x = []
    y = []
    for i, val in enumerate(encoded):
        x.extend([i * bits_per_symbol, (i + 1) * bits_per_symbol])
        y.extend([val, val])
    x.pop(0)
    y.pop(0)

    # Plotting
    plt.figure(figsize=(10, 3))
    plt.step(x, y, where='post', linewidth=2)
    plt.title(f"{title} Encoding", fontsize=14)
    plt.ylim(-2, 2)
    plt.grid(True)
    plt.xlabel("Time")
    plt.ylabel("Voltage")

    # Binary labels
    spacing = 2 if paired else 1
    for i, bit in enumerate(data):
        x_pos = i * bits_per_symbol * spacing + (bits_per_symbol * spacing / 2)
        plt.text(x_pos, 1.5, str(bit), ha='center', fontsize=12, color='blue')

    plt.tight_layout()
    plt.show()

# ---------- Main Section ----------

data = [1, 0, 1, 1, 0, 0, 1]  # Sample binary input

plot_encoding(data, unipolar_nrz, "Unipolar NRZ")
plot_encoding(data, polar_nrz, "Polar NRZ (NRZ-L)")
plot_encoding(data, nrzi, "NRZ-I")
plot_encoding(data, rz, "RZ", bits_per_symbol=0.5, paired=False)
plot_encoding(data, manchester, "Manchester", bits_per_symbol=0.5, paired=True)
plot_encoding(data, diff_manchester, "Differential Manchester", bits_per_symbol=0.5, paired=True)
plot_encoding(data, ami, "AMI")
plot_encoding(data, bipolar_rz, "Bipolar RZ", bits_per_symbol=0.5, paired=True)