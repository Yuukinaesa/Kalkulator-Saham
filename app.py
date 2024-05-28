import streamlit as st

def calculate_profit_loss(jumlah_lot, harga_beli, harga_jual, fee_beli, fee_jual):
    total_beli = jumlah_lot * 100 * harga_beli
    total_jual = jumlah_lot * 100 * harga_jual

    fee_beli_total = total_beli * fee_beli
    fee_jual_total = total_jual * fee_jual

    total_beli += fee_beli_total
    total_jual -= fee_jual_total

    profit_loss = total_jual - total_beli
    profit_loss_percentage = (profit_loss / total_beli) * 100 if total_beli != 0 else 0

    return total_beli, total_jual, profit_loss, profit_loss_percentage, fee_beli_total, fee_jual_total

def ipot_page():
    st.header("IPOT / Indo Premier Sekuritas")
    jumlah_lot = st.number_input("Jumlah Lot:", min_value=0, step=1, format="%d")
    harga_beli = st.number_input("Harga Beli (per saham):", min_value=0.0, step=1000.0, format="%.0f")
    harga_jual = st.number_input("Harga Jual (per saham):", min_value=0.0, step=1000.0, format="%.0f")
    include_fee_beli = st.checkbox("Masukkan Fee Beli (0,19%)")
    include_fee_jual = st.checkbox("Masukkan Fee Jual (0,29%)")

    if st.button("Hitung"):
        if jumlah_lot >= 0 and harga_beli >= 0 and harga_jual >= 0:
            fee_beli = 0.0019 if include_fee_beli else 0
            fee_jual = 0.0029 if include_fee_jual else 0
            total_beli, total_jual, profit_loss, profit_loss_percentage, fee_beli_total, fee_jual_total = calculate_profit_loss(jumlah_lot, harga_beli, harga_jual, fee_beli, fee_jual)
            st.write(f"Total Beli: Rp {total_beli:,.0f} (termasuk fee: Rp {fee_beli_total:,.0f})")
            st.write(f"Total Jual: Rp {total_jual:,.0f} (termasuk fee: Rp {fee_jual_total:,.0f})")
            st.write(f"Profit/Loss: Rp {profit_loss:,.0f}")
            st.write(f"Profit/Loss (%): {profit_loss_percentage:.2f}%")
            if profit_loss > 0:
                st.success("Profit!")
            elif profit_loss < 0:
                st.error("Loss!")
            else:
                st.info("Break Even!")
        else:
            st.warning("Harap masukkan semua nilai dengan benar.")

def stockbit_page():
    st.header("Stockbit / Bibit")
    jumlah_lot = st.number_input("Jumlah Lot:", min_value=0, step=1, format="%d")
    harga_beli = st.number_input("Harga Beli (per saham):", min_value=0.0, step=1000.0, format="%.0f")
    harga_jual = st.number_input("Harga Jual (per saham):", min_value=0.0, step=1000.0, format="%.0f")
    include_fee_beli = st.checkbox("Masukkan Fee Beli (0,15%)")
    include_fee_jual = st.checkbox("Masukkan Fee Jual (0,25%)")

    if st.button("Hitung"):
        if jumlah_lot >= 0 and harga_beli >= 0 and harga_jual >= 0:
            fee_beli = 0.0015 if include_fee_beli else 0
            fee_jual = 0.0025 if include_fee_jual else 0
            total_beli, total_jual, profit_loss, profit_loss_percentage, fee_beli_total, fee_jual_total = calculate_profit_loss(jumlah_lot, harga_beli, harga_jual, fee_beli, fee_jual)
            st.write(f"Total Beli: Rp {total_beli:,.0f} (termasuk fee: Rp {fee_beli_total:,.0f})")
            st.write(f"Total Jual: Rp {total_jual:,.0f} (termasuk fee: Rp {fee_jual_total:,.0f})")
            st.write(f"Profit/Loss: Rp {profit_loss:,.0f}")
            st.write(f"Profit/Loss (%): {profit_loss_percentage:.2f}%")
            if profit_loss > 0:
                st.success("Profit!")
            elif profit_loss < 0:
                st.error("Loss!")
            else:
                st.info("Break Even!")
        else:
            st.warning("Harap masukkan semua nilai dengan benar.")

# Sidebar menu
menu_selection = st.sidebar.radio("Pilih Menu:", ("Welcome", "IPOT / Indo Premier Sekuritas", "Stockbit / Bibit"))

# Routing based on menu selection
if menu_selection == "Welcome":
    st.title("Welcome!")
    st.write(" Selamat datang di aplikasi kalkulator profit/loss saham. ")
    st.write(" 👈 Silahkan pilih aplikasi yang digunakan pada menu sidebar. 👈")
elif menu_selection == "IPOT / Indo Premier Sekuritas":
    ipot_page()
elif menu_selection == "Stockbit / Bibit":
    stockbit_page()
