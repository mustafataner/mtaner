import streamlit as st

st.balloons()
def main():
    # Başlık
    st.title("Bir Bilim Adamının Aşkı: Mustafa Taner'in Merviş Hormonu Keşfi")

    # Metni gösterme
    if st.button("Oku"):
        metin = """
       

Bir zamanlar, bilim dünyasının önde gelen isimlerinden biri olan Dr. Mustafa Taner, sıradışı bir keşfe imza attı. Fakat bu keşif, sadece laboratuvarların soğuk duvarlarında gerçekleşen bir buluş değildi; bu keşif, kalbinin derinliklerinden yükselen bir aşkın ve Merve'nin gizemli dünyasının bir yansımasıydı.

Dr. Mustafa Taner, genç bir bilim insanı olarak hayatına, laboratuvarında yaptığı araştırmalarla yön veriyordu. Ancak bir gün, işte o gün, her şey değişti. Laboratuvarında çalışırken, bir anlığına gözlerini kapattığında Merve'nin yüzünü görebiliyordu. Merve'nin gülüşü, odasını aydınlatıyordu sanki. İşte o an, bilimsel bir keşfin kapısını aralamak için ilhamın gelip ona yüksek sesle kapıyı çaldığı andı.

Merve'ye duyduğu derin sevgi ve onunla geçirdiği her an, Dr. Taner'in zihninde yeni bir sorunun cevabını aramasına neden oldu: Aşkın biyolojik temeli ne olabilir? İşte bu soru, onu Merviş Hormonu'na götüren yolu açtı.

Araştırmaları, duygusal bağların ve aşkın kimyasal temellerini anlamaya odaklandı. Her şey, Merve'nin kokusunu duyduğunda veya onunla geçirdiği uzun ve keyifli sohbetlerde zamanın nasıl durduğunu fark ettiği bir anla başladı. Beyninin laboratuvarında çalıştığı gibi çalışmaya başladığı anlardı bunlar.

Ve nihayet, laboratuvarındaki deneylerinde, beyindeki duygusal tepkileri tetikleyen ve aşkın kimyasal simgesi haline gelen bir hormon keşfetti. Adını da Merviş Hormonu koydu; çünkü bu hormon, Merve'nin onun için ifade ettiği duygusal bağı ve aşkı simgeliyordu.

Dr. Mustafa Taner, bu keşfiyle sadece bilime ışık tutmamıştı; aynı zamanda kalbinin en derin köşelerindeki aşkı da herkese göstermişti. Onun için artık bilim, sadece denklemlerin ve deneylerin ötesinde bir anlam taşıyordu: Sevginin, tutkunun ve Merve'nin ışığının bir yansımasıydı.

Böylece, bilim ve aşkın buluştuğu muhteşem bir hikaye, Dr. Mustafa Taner'in Merviş Hormonu keşfiyle yazıldı. Bu keşif, sadece laboratuvarlarını değil, kalpleri de ısıttı. Çünkü bazen, bilim insanlarının en büyük keşifleri, kalplerinin sesini dinlemeleri ve sevdikleriyle aralarındaki bağı hissetmeleriyle başlar.
        """

        # Metni renkli ve stilize olarak gösterme
        styled_text = metin.replace("Merve'nin gülüşü", '<span style="color:pink;font-weight:bold;" title="Dr. Mustafa Taner">Merve\'nin gülüşü</span>')
        styled_text = styled_text.replace("Merve'nin kokusu", '<span style="color:pink;font-weight:bold;" title="Merve\'nin kokusu">Merve\'nin kokusu</span>')

        st.markdown(styled_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
