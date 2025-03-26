from lib.lib_show_iq_wave import show_iq_two_channels
import argparse

def main():
    parser = argparse.ArgumentParser(description="繪製 I/Q 數據波形")
    parser.add_argument("filename", type=str, help="輸入的 .dat 檔案路徑")
    args = parser.parse_args()

    length = int(3e4)
    shift = length
    show_iq_two_channels(args.filename, shift, length)

# Usage:
# python show-iq.py ./20250225/iq_f2.4_bw20m_g0_d3m_S45
# python main_show_iq_show_two_channels.py "D:\work\project\20.06.4-CUAS-Passive radar phase I\receiver\data\20250225\iq_f2.4_bw20m_g0_d3m_S45"
# python main_show_iq_show_two_channels.py "../../../data/rx_data_dual"
if __name__ == "__main__":
    main()