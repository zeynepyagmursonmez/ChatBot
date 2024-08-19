yanitlar = {
    "merhaba": "Merhaba! Nasılsın?",
    "nasılsın": "İyiyim, teşekkürler. Sen nasılsın?",
    "iyiyim": "Harika! Başka ne sormak istersin?",
    "teşekkürler": "Rica ederim!",
    "görüşürüz": "Görüşmek üzere!"
}

def chatbot_yaniti(soru):
    soru = soru.lower()
    if soru in yanitlar:
        return yanitlar[soru]
    else:
        return "Üzgünüm, bu soruya cevap veremem. Başka bir soru sorabilir misin?"

while True:
    soru = input("Soru: ")
    yanit = chatbot_yaniti(soru)
    print("Chatbot: ", yanit)
