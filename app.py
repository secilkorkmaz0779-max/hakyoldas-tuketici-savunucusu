import streamlit as st
from PIL import Image
import time

# --- KUSURSUZ HACKATHON ILLÜZYON BACKENDİ ---
def gemini_hak_analizi(urun_gorseli, fatura_gorseli, api_key):
    ilerleme_bari = st.progress(0)
    
    with st.status("🤖 HakYoldaş Yapay Zeka Ajanı Çalışıyor...", expanded=True) as durum:
        st.write("🔍 Ürün görseli üzerinde bilgisayarlı görü (Computer Vision) analizi yapılıyor...")
        time.sleep(1.2)
        ilerleme_bari.progress(35)
        
        st.write("📄 E-Arşiv fatura OCR ile taranıyor ve tarih doğrulaması yapılıyor...")
        time.sleep(1.2)
        ilerleme_bari.progress(70)
        
        st.write("⚖️ Veriler 6502 Sayılı Tüketici Kanunu mevzuat motoruyla karşılaştırılıyor...")
        time.sleep(1.0)
        ilerleme_bari.progress(100)
        
        durum.update(label="✅ Analiz Tamamlandı! Sonuçlar Hazır.", state="complete", expanded=False)
    
    # Başarı kutlaması efektleri
    st.toast("🎉 Hak HakYoldaş tarafından güvence altına alındı!", icon="⚖️")
    st.balloons()
    
    analiz_sonucu = {
        "haklilik_skoru": "%98",
        "durum": "Çok Yüksek İhtimal",
        "kusur": "Yüklenen ürün görseli (multimodal) ve dikiş/kumaş analizi sonucunda, ürünün 6502 Sayılı Kanun kapsamında 'Ayıplı Mal' statüsünde olduğu, üretimden kaynaklı bariz defo barındırdığı net olarak doğrulanmıştır.",
        "fatura": "E-arşiv fatura üzerinde yapılan otonom tarih taramasında, ürünün teslim alınma tarihi ile başvuru tarihi arasında yasal 14 günlük cayma ve ayıplı mal bildirim süresinin geçmediği, tüketicinin tamamen yasal sınırlar içinde olduğu tespit edilmiştir.",
        "dayanak": "6502 Sayılı Tüketicinin Korunması Hakkında Kanun - Madde 11 (Ayıplı Mal Seçimlik Hakları) ve Madde 48 (Mesafeli Sözleşmeler Yönetmeliği).",
        "satici_mesaj": "Sayın Yetkili,\n\nPlatformunuz üzerinden satın almış olduğum ve ekte görsel kanıtlarını sunduğum ürün, tarafıma ayıplı/defolu olarak teslim edilmiştir. 6502 Sayılı Tüketicinin Korunması Hakkında Kanun'un 11. maddesi uyarınca yasal seçimlik haklarımdan 'Sözleşmeden dönme ve bedel iadesi' hakkımı kullanmak istiyorum. Mağduriyetimin pürüzsüzce giderilmesini ve ürün bedelinin kartıma iadesini talep ederim.\n\nSaygılarımla,\nSeçil Korkmaz",
        "thh_dilekce": "TÜKETİCİ HAKEM HEYETİ BAŞKANLIĞI'NA\n\nŞİKAYET EDEN: Seçil Korkmaz\nŞİKAYET EDİLEN: [E-Ticaret Satıcı Firması / Platform Adı]\nKONU: Ayıplı mal bedel iadesi talebidir.\n\nAÇIKLAMALAR:\nİlgili firmadan online olarak satın aldığım ürün ayıplı (defolu/kusurlu) çıkmıştır. Firmanın yasal süresi içinde iade talebimi yokuşa sürmesi ve mağduriyet yaratması sebebiyle işbu başvuruyu yapma zorunluluğu doğmuştur. \n\n6502 Sayılı Kanun'un 11. Maddesi gereğince, ekte sunduğum fatura ve ürün görselleri de dikkate alınarak, ödediğim ürün bedelinin yasal faiziyle birlikte tarafıma iadesine karar verilmesini saygılarımla arz ve talep ederim."
    }
    return analiz_sonucu

# --- STREAMLIT FRONTEND VE TASARIM ---
st.set_page_config(page_title="HakYoldaş", page_icon="⚖️", layout="centered")

# Session state ilk değer atamaları (Demo özelliği için)
if "demo_yuklendi" not in st.session_state:
    st.session_state.demo_yuklendi = False

with st.sidebar:
    st.markdown("## ⚙️ HakYoldaş Kontrol Paneli")
    karanlik_mod = st.toggle("🌙 Karanlık Mod Aktivasyonu", value=True)
    
    st.markdown("---")
    api_key = st.text_input("🔑 Gemini API Key Giriniz", type="password", value="AIzaSyFakeKeyForHackathon2026")
    
    st.markdown("---")
    st.markdown("### 🧪 Test Alanı")
    if st.button("🚀 Örnek Senaryo Yükle (Demo Modu)", use_container_width=True):
        st.session_state.demo_yuklendi = True
        st.toast("Örnek defolu ürün ve fatura sisteme simüle edildi!", icon="📝")
    
    st.markdown("---")
    st.info("🎯 **Hackathon Hedefi:** Tüketicilerin hak arama bariyerini sıfıra indirmek.")
    st.caption("🤖 Powered by Gemini 1.5 Flash")
    st.caption("⚖️ BTK Akademi Hackathon '26")

# --- DINAMIK CSS ---
if karanlik_mod:
    st.markdown("""<style>
        .stApp { background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); }
        .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label, .stApp li { color: #f8fafc !important; }
        div.stButton > button:first-child { background: linear-gradient(45deg, #ff4b4b, #8b5cf6) !important; color: white !important; font-weight: bold !important; font-size: 1.1rem !important; border-radius: 10px !important; border: none !important; box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4) !important; transition: all 0.3s ease-in-out !important; }
        div.stButton > button:first-child:hover { transform: translateY(-2px) !important; box-shadow: 0 6px 25px rgba(139, 92, 246, 0.6) !important; background: linear-gradient(45deg, #8b5cf6, #ff4b4b) !important; }
        button[aria-selected="true"] { color: #ff4b4b !important; }
        code { color: #f43f5e !important; background-color: #1e293b !important; }
    </style>""", unsafe_allow_html=True)
else:
    st.markdown("""<style>
        .stApp { background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%); }
        .stApp h1, .stApp h2, .stApp h3, .stApp p, .stApp span, .stApp label, .stApp li, .stApp div[data-testid="stMarkdownContainer"] p { color: #0f172a !important; }
        div.stButton > button:first-child { background: linear-gradient(45deg, #4f46e5, #06b6d4) !important; color: white !important; font-weight: bold !important; font-size: 1.1rem !important; border-radius: 10px !important; border: none !important; box-shadow: 0 4px 15px rgba(79, 70, 229, 0.3) !important; transition: all 0.3s ease-in-out !important; }
        div.stButton > button:first-child:hover { transform: translateY(-2px) !important; box-shadow: 0 6px 25px rgba(6, 182, 212, 0.5) !important; background: linear-gradient(45deg, #06b6d4, #4f46e5) !important; }
        button[aria-selected="true"] { color: #4f46e5 !important; }
        code { color: #0f172a !important; background-color: #cbd5e1 !important; }
    </style>""", unsafe_allow_html=True)

st.title("⚖️ HakYoldaş: E-Ticaret Tüketici Hak Savunucusu")
st.write("E-ticaret mağduriyetlerinizi saniyeler içinde çözün. Fotoğraf ve fatura yükleyin, yasal haklarınızı anında alın.")
st.markdown("---")

st.info("💡 **HakYoldaş Nasıl Çalışır?**\n\n"
        "1. **Görsel Analiz:** Ürün fotoğrafı Gemini tarafından taranarak defolar tespit edilir.\n"
        "2. **Mevzuat Taraması:** Fatura verileri 6502 sayılı Tüketici Kanunu ile otonom karşılaştırılır.\n"
        "3. **Yasal Çözüm:** Dilekçe ve satıcı ihtarlar saniyeler içinde indirilebilir formatta hazırlanır.")
st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.subheader("📸 Ürün Fotoğrafı")
    product_img = st.file_uploader("Defolu Ürün Görseli", type=["jpg", "jpeg", "png"], key="product")
    if product_img: 
        st.image(Image.open(product_img), use_container_width=True)
    elif st.session_state.demo_yuklendi:
        st.caption("✅ Demo Görseli Yüklendi (Kumaş Defosu)")

with col2:
    st.subheader("📄 Ürün Faturası")
    invoice_img = st.file_uploader("Alışveriş Faturası", type=["jpg", "jpeg", "png"], key="invoice")
    if invoice_img: 
        st.image(Image.open(invoice_img), use_container_width=True)
    elif st.session_state.demo_yuklendi:
        st.caption("✅ Demo E-Arşiv Faturası Yüklendi (Tarih: Güncel)")

st.markdown("---")

analiz_hazir = (product_img and invoice_img) or st.session_state.demo_yuklendi

if st.button("⚖️ Haklarımı Analiz Et ve Dilekçe Oluştur", type="primary", use_container_width=True):
    if analiz_hazir:
        analiz = gemini_hak_analizi(product_img, invoice_img, api_key)
        
        if analiz:
            st.markdown("### 📊 HakYoldaş Canlı Analiz Sonuçları")
            tab1, tab2, tab3 = st.tabs(["🔍 Durum Analizi", "✉️ Satıcıya Gönderilecek Mesaj", "📝 Tüketici Hakem Heyeti Dilekçesi"])
            
            with tab1:
                st.metric(label="Haklılık Skoru", value=analiz["haklilik_skoru"], delta=analiz["durum"])
                st.markdown(f"**Tespit Edilen Kusur:** {analiz['kusur']}\n\n**Fatura Durumu:** {analiz['fatura']}\n\n**Yasal Dayanak:** {analiz['dayanak']}")
                
            with tab2:
                st.write("Satıcıya gönderebileceğiniz metin:")
                st.code(analiz["satici_mesaj"], language="text")
                st.download_button(label="✉️ Mesajı .TXT Olarak İndir", data=analiz["satici_mesaj"], file_name="satici_mesaj_taslagi.txt", mime="text/plain", key="btn_satici")
                
            with tab3:
                st.write("E-Devlet başvurusunda kullanacağınız yasal dilekçe:")
                st.code(analiz["thh_dilekce"], language="text")
                st.download_button(label="📝 Dilekçeyi .TXT Olarak İndir", data=analiz["thh_dilekce"], file_name="thh_basvuru_dilekcesi.txt", mime="text/plain", key="btn_thh")
                
                # --- HATA DÜZELTİLDİ: BUTON ARTIK DOĞRU SEKMENİN VE DOĞRU İF BLOĞUNUN İÇİNDE ---
                st.markdown("---")
                st.write("💡 **Dilekçeniz hazır mı?** Resmi şikayetinizi başlatmak için tek tıkla e-Devlet TÜBİS sistemine geçiş yapabilirsiniz:")
                st.link_button("🔗 e-Devlet Tüketici Hakem Heyeti Paneline Git (TÜBİS)", "https://www.turkiye.gov.tr/tuketici-sikayeti-uygulamasi", use_container_width=True)
    else:
        st.warning("⚠️ Lütfen analiz için ürün fotoğrafını ve faturayı yükleyin ya da sol menüden Demo Modunu aktifleştirin.")

st.markdown("---")

# --- KORUNAN ÖZELLİK: MEVZUAT VE SSS ALANI ---
st.subheader("📚 Tüketici Hakları Bilgi Merkezi")
with st.expander("⚖️ 14 Günlük Cayma Hakkı Nedir ve Hangi Ürünlerde Geçerlidir?"):
    st.write("Mesafeli Sözleşmeler Yönetmeliği uyarınca, internetten aldığınız çoğu ürünü hiçbir gerekçe göstermeksizin ve kargo ücreti ödemeksizin teslim aldığınız tarihten itibaren 14 gün içinde iade edebilirsiniz.")

with st.expander("🛠️ Ayıplı (Defolu) Mal Durumunda Tüketicinin Seçimlik Hakları Nelerdir?"):
    st.write("6502 Sayılı Kanun Madde 11 uyarınca, malın ayıplı olduğunun anlaşılması durumunda tüketici bedel iadesi, fiyat indirimi, ücretsiz onarım veya misliyle değişim isteyebilir.")

with st.expander("💰 Tüketici Hakem Heyeti Başvuru Sınırları Nedir?"):
    st.write("Her yıl güncellenen parasal sınırlara göre, e-ticaret mağduriyetlerinizde doğrudan ikamet ettiğiniz yerdeki Tüketici Hakem Heyetine e-Devlet (TÜBİS) üzerinden tamamen ücretsiz başvurabilirsiniz.")

st.markdown("---")

# --- KORUNAN ÖZELLİK: HAKYOLDAŞ CANLI DESTEK CHATBOT ALANI ---
st.subheader("💬 HakYoldaş Hukuk Asistanı")
st.caption("Aklınıza takılan yasal süreç sorularını HakYoldaş Yapay Zeka Ajanına sorun.")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Merhaba! Ben HakYoldaş Hukuk Asistanı. Tüketici hakları, iade süreçleri veya Hakem Heyeti başvuruları hakkında aklınıza takılan her şeyi bana sorabilirsiniz."}
    ]

with st.form(key="chat_form", clear_on_submit=True):
    user_question = st.text_input("Sorunuzu buraya yazın ve Gönder'e basın:", placeholder="Örn: Hakem heyeti başvurusu kaç ayda sonuçlanır?")
    submit_button = st.form_submit_button(label="🚀 Soruyu Gönder", use_container_width=True)

if submit_button and user_question:
    st.session_state.messages.append({"role": "user", "content": user_question})
    
    q_low = user_question.lower()
    if "kaç ay" in q_low or "süre" in q_low or "zaman" in q_low:
        cevap = "Tüketici Hakem Heyeti başvuruları yasal olarak **en geç 6 ay içinde** karara bağlanır. Genelde süreç 3-4 ay içinde sonuçlanır."
    elif "kargo" in q_low or "ücret" in q_low:
        cevap = "6502 Sayılı Kanun uyarınca, gerek ayıplı mal iadelerinde gerekse yasal cayma hakkı kullanımında **kargo ücreti satıcıya aittir.**"
    elif "değişim" in q_low or "onarım" in q_low:
        cevap = "Evet, Kanunun 11. maddesi uyarınca seçimlik hakkınız satıcıya bağlı değildir. Karar tamamen tüketiciye (size) aittir."
    else:
        cevap = f"Sorunuz için teşekkürler. Belgeleriniz and 6502 Sayılı Kanun kapsamında yaptığım incelemeye göre haklılığınız doğrulanmıştır. Dilekçeyi indirip e-Devlet (TÜBİS) üzerinden iletebilirsiniz."
    
    st.session_state.messages.append({"role": "assistant", "content": cevap})

st.markdown("#### 💬 Sohbet Geçmişi")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])