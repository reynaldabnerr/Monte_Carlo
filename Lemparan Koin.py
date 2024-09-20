import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def lempar_koin():
    """Fungsi untuk melempar koin dan mengembalikan hasilnya."""
    return 'kepala' if random.randint(0, 1) == 0 else 'ekor'

def simulasi_monte_carlo(n_lemparan):
    """Simulasi Monte Carlo untuk menghitung probabilitas mendapatkan kepala."""
    jumlah_kepala = 0
    hasil_probabilitas = []

    for i in range(1, n_lemparan + 1):
        if lempar_koin() == 'kepala':
            jumlah_kepala += 1
        
        # Menyimpan hasil probabilitas setiap iterasi
        if i % 100 == 0:  # Menyimpan setiap 100 lemparan untuk mengurangi data
            probabilitas_kepala = jumlah_kepala / i
            hasil_probabilitas.append((i, probabilitas_kepala))

    return hasil_probabilitas

# Jumlah lemparan koin dalam simulasi
n_lemparan = 10000

# Melakukan simulasi
hasil_probabilitas = simulasi_monte_carlo(n_lemparan)

# Memisahkan data untuk grafik
jumlah_lemparan, probabilitas = zip(*hasil_probabilitas)

# Membuat grafik
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], label='Probabilitas Kepala', color='blue')
ax.axhline(y=0.5, color='red', linestyle='--', label='Probabilitas Teoritis (0.5)')
ax.set_xlabel('Jumlah Lemparan')
ax.set_ylabel('Probabilitas Kepala')
ax.set_title('Simulasi Monte Carlo: Probabilitas Kepala vs Jumlah Lemparan')
ax.legend()
ax.grid(True)

def init():
    """Inisialisasi grafik kosong."""
    ax.set_xlim(0, n_lemparan)
    ax.set_ylim(0, 1)
    return line,

def update(frame):
    """Update grafik untuk frame tertentu."""
    line.set_data(jumlah_lemparan[:frame], probabilitas[:frame])
    return line,

# Interval diatur menjadi 50 ms untuk animasi lebih perlahan
ani = animation.FuncAnimation(fig, update, frames=len(jumlah_lemparan), init_func=init, blit=True, interval=50, repeat=False)

plt.show()