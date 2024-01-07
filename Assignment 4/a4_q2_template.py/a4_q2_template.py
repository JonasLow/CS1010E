def filter_wave(wave, n):
    for _ in range(n):
        new_wave = [0] * len(wave)
        for i in range(len(wave)):
            if (i == 0 and len(wave) > i + 1):
                new_wave[i] = wave[i]*0.6 + wave[i+1]*0.2
            elif len(wave) == i + 1:
                new_wave[i] = wave[i-1] * 0.2 + wave[i]*0.6
            else:
                new_wave[i] = wave[i-1] * 0.2 + wave[i]*0.6 + wave[i+1]*0.2
            i += 1
        wave = new_wave
    return wave

if __name__ == "__main__":
    # Sample original wave
    original_wave = [0, 1, 3, 5, 4 ,2 ,0]
    # n is set as 1
    print(filter_wave(original_wave, 1))
