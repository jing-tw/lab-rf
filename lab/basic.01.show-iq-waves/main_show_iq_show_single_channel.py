from lib.lib_show_iq_wave import show_iq_one_channel
import argparse

def main():
    parser = argparse.ArgumentParser(description="繪製 I/Q 數據波形")
    parser.add_argument("filename", type=str, help="輸入的 .dat 檔案路徑")
    args = parser.parse_args()

    length = int(100e3)
    shift = 0
    show_iq_one_channel(args.filename, shift, length)

# Usage:
# python main_show_iq_show_single_wave.py "D:\work\project\20.06.4-CUAS-Passive radar phase I\receiver\data\20250325\b210_freq2.4g_bw50m.dat"
if __name__ == "__main__":
    main()