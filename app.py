import streamlit as st

def calculate_profit_loss(jumlah_lot, harga_beli, harga_jual, fee_beli, fee_jual):
    total_beli = jumlah_lot * 100 * harga_beli * (1 + fee_beli)
    total_jual = jumlah_lot * 100 * harga_jual * (1 - fee_jual)
    profit_loss = total_jual - total_beli
    profit_loss_percentage = (profit_loss / total_beli) * 100 if total_beli else 0
    return total_beli, total_jual, profit_loss, profit_loss_percentage

def calculate_dividend(jumlah_lot, dividen_per_saham):
    total_dividen = jumlah_lot * dividen_per_saham * 100
    return total_dividen

def calculate_dividend_yield(dividen_per_saham, harga_beli):
    dividend_yield = (dividen_per_saham / harga_beli) * 100
    return dividend_yield

def stock_page(title, fee_beli, fee_jual):
    st.header(title)
    jumlah_lot = st.number_input("Jumlah Lot:", min_value=0, step=1, format="%d")
    harga_beli = st.number_input("Harga Beli (per saham):", min_value=0.0, step=1000.0, format="%.0f")
    harga_jual = st.number_input("Harga Jual (per saham):", min_value=0.0, step=1000.0, format="%.0f")
    include_fee_beli = st.checkbox("Masukkan Fee Beli")
    include_fee_jual = st.checkbox("Masukkan Fee Jual")
    include_dividend = st.checkbox("Masukkan Dividen")

    if include_dividend:
        dividen_per_saham_input = st.number_input("Dividen per Saham:", min_value=0, step=1, format="%d")
        if jumlah_lot > 0 and harga_beli > 0:
            total_dividen = calculate_dividend(jumlah_lot, dividen_per_saham_input)
            dividend_yield = calculate_dividend_yield(dividen_per_saham_input, harga_beli)
            st.write(f"Total Dividen: Rp {total_dividen:,.0f}")
            st.write(f"Dividend Yield: {dividend_yield:.2f}%")
        else:
            st.warning("Harap masukkan jumlah lot dan harga beli yang benar untuk menghitung dividen.")

    if st.button("Hitung"):
        if jumlah_lot >= 0 and harga_beli >= 0 and harga_jual >= 0:
            fee_beli = fee_beli if include_fee_beli else 0
            fee_jual = fee_jual if include_fee_jual else 0
            total_beli, total_jual, profit_loss, profit_loss_percentage = calculate_profit_loss(jumlah_lot, harga_beli, harga_jual, fee_beli, fee_jual)
            st.write(f"Total Beli: Rp {total_beli:,.0f}")
            st.write(f"Total Jual: Rp {total_jual:,.0f}")
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
menu_selection = st.sidebar.radio("Pilih Menu:", ("Welcome", "IPOT / Indo Premier Sekuritas", "Stockbit / Bibit", "BNI Bions"))

# Routing based on menu selection
if menu_selection == "Welcome":
    st.title("Welcome!")
    st.write("Selamat datang di aplikasi kalkulator profit/loss saham.")
    st.write("👈 Silahkan pilih aplikasi yang digunakan pada menu sidebar. 👈")
elif menu_selection == "IPOT / Indo Premier Sekuritas":
    stock_page("IPOT / Indo Premier Sekuritas", 0.0019, 0.0029)
elif menu_selection == "Stockbit / Bibit":
    stock_page("Stockbit / Bibit", 0.0015, 0.0025)
elif menu_selection == "BNI Bions":
    stock_page("BNI Bions", 0.0017, 0.0027)
