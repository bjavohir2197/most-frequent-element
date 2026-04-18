def eng_ko_p_u_chraydigan_elementni_toping(sarlavha, matn):
    sarlavha_sozlari = sarlavha.split()
    matn_sozlari = matn.split()
    sarlavha_sozlari_kopayish = {}
    matn_sozlari_kopayish = {}

    for soz in sarlavha_sozlari:
        if soz in sarlavha_sozlari_kopayish:
            sarlavha_sozlari_kopayish[soz] += 1
        else:
            sarlavha_sozlari_kopayish[soz] = 1

    for soz in matn_sozlari:
        if soz in matn_sozlari_kopayish:
            matn_sozlari_kopayish[soz] += 1
        else:
            matn_sozlari_kopayish[soz] = 1

    barcha_sozlar = {**sarlavha_sozlari_kopayish, **matn_sozlari_kopayish}
    eng_ko_p_u_chraydigan_element = max(barcha_sozlar, key=barcha_sozlar.get)

    return eng_ko_p_u_chraydigan_element

sarlavha = "Eng ko'p uchraydigan elementni toping"
matn = "Eng ko'p uchraydigan elementni toping bu masala"
print(eng_ko_p_u_chraydigan_elementni_toping(sarlavha, matn))
