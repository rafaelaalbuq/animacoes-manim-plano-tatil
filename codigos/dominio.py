from manim import *
import numpy as np

class dominio(MovingCameraScene):
    def construct(self):
        # 1. Configuração de Fundo e Logo
        cordefundo = ManimColor("#D5D5DD")
        self.camera.background_color = cordefundo

        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff=0.1)
            self.add(img)
        except:
            print('LOGO NAO ENCONTRADA')


        titulo = Tex(r"Domínio, Contradomínio e Imagem", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))


        dom_elipse = Ellipse(width=3, height=6, color=PURE_GREEN, fill_opacity=0).shift(LEFT*3)
        codom_elipse = Ellipse(width=3, height=6, color=PURE_BLUE, fill_opacity=0).shift(RIGHT*3)
        ima_elipse = Ellipse(width=1.2, height=3, color=PURE_RED, fill_opacity=0)

        label_dom = Tex("Domínio", color=PURE_GREEN).scale(1.5).next_to(dom_elipse, UP)
        label_codom = Tex("Contradomínio", color=PURE_BLUE).scale(1.5).next_to(codom_elipse, UP)
      
       
        elementos_dom = VGroup(
            Tex(r'2'), Tex(r'3'), Tex(r'4')
        ).set_color(PURE_GREEN).scale(1.5).arrange(DOWN, buff=0.5).move_to(dom_elipse.get_center())

        elementos_codom = VGroup(
            Tex(r'4'), Tex(r'6'), Tex(r'8'), Tex(r'10')
        ).set_color(PURE_BLUE).scale(1.5).arrange(DOWN, buff=0.5).move_to(codom_elipse.get_center())

       
        ima_elipse.move_to(elementos_codom[1].get_center())
        label_ima = Tex("Imagem", color=PURE_RED).scale(1.2).next_to(ima_elipse, RIGHT*2, buff=0.5)
       

        #setas
        seta_2_4 = Arrow(start=elementos_dom[0].get_right(), end=elementos_codom[0].get_left(), color=BLACK)
        seta_3_6 = Arrow(start=elementos_dom[1].get_right(), end=elementos_codom[1].get_left(), color=BLACK)
        seta_4_8 = Arrow(start=elementos_dom[2].get_right(), end=elementos_codom[2].get_left(), color=BLACK)

        self.play(Create(dom_elipse), Create(codom_elipse))
        self.play(Write(label_dom), Write(label_codom))
        self.play(FadeIn(elementos_dom), FadeIn(elementos_codom))
        self.wait()
        self.play(Create(seta_2_4), Create(seta_3_6), Create(seta_4_8))
        self.wait()
        self.play(Create(ima_elipse), Write(label_ima))
        self.wait(3)

        #fadeout
        self.play(FadeOut(dom_elipse, codom_elipse, ima_elipse, label_dom, label_codom, label_ima, elementos_dom, elementos_codom, seta_2_4, seta_3_6, seta_4_8))
        self.wait()


        #funcao injetora, bijetora e sobrejetora

        #injetora

        
        titulo = Tex(r"Função Injetora", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.wait()
        self.play(titulo.animate.to_corner(DOWN+LEFT, buff=0.2))


        elementos_dom_IN = VGroup(
            Tex(r'2'), Tex(r'3'), Tex(r'4')
        ).set_color(PURE_GREEN).scale(1.5).arrange(DOWN, buff=0.5).move_to(dom_elipse.get_center())

        elementos_codom_IN = VGroup(
            Tex(r'4').set_color(PURE_BLUE), 
            Tex(r'6').set_color(PURE_BLUE), 
            Tex(r'8').set_color(PURE_BLUE), 
            Tex(r'10').set_color(PURE_BLUE)
        ).scale(1.5).arrange(DOWN, buff=0.5).move_to(codom_elipse.get_center())

        self.play(Create(dom_elipse), Create(codom_elipse))
        self.play(Write(label_dom), Write(label_codom))
        self.play(FadeIn(elementos_dom_IN), FadeIn(elementos_codom_IN))
        self.wait()
        self.play(Create(seta_2_4), Create(seta_3_6), Create(seta_4_8))
        #mudar a cor do elemento 10 do contradomínio para indicar que não tem imagem
        self.play(elementos_codom_IN[3].animate.set_color(YELLOW))
        self.wait()
        self.play(Create(ima_elipse), Write(label_ima))
        self.wait(3)
        self.play(FadeOut(dom_elipse, codom_elipse, ima_elipse, label_dom, label_codom, label_ima, elementos_dom_IN, elementos_codom_IN, seta_2_4, seta_3_6, seta_4_8, titulo))
        self.wait()

        #sobrejetora
        titulo = Tex(r"Função Sobrejetora", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.play(titulo.animate.to_corner(DOWN+LEFT, buff=0.2))
        self.wait()

        elementos_dom_SOB = VGroup(
            Tex(r'2'), Tex(r'-2'), Tex(r'3'), Tex(r'5')
        ).set_color(PURE_GREEN).scale(1.5).arrange(DOWN, buff=0.5).move_to(dom_elipse.get_center())

        elementos_codom_SOB = VGroup(
            Tex(r'4').set_color(PURE_BLUE), 
            Tex(r'9').set_color(PURE_BLUE), 
            Tex(r'25').set_color(PURE_BLUE)
        ).scale(1.5).arrange(DOWN, buff=0.5).move_to(codom_elipse.get_center())

        ima_elipse.move_to(elementos_codom_SOB[1].get_center())
        

        seta_2_4_SOB = Arrow(start=elementos_dom_SOB[0].get_right(), end=elementos_codom_SOB[0].get_left(), color=BLACK)
        seta_m2_4_SOB = Arrow(start=elementos_dom_SOB[1].get_right(), end=elementos_codom_SOB[0].get_left(), color=BLACK)
        seta_3_9_SOB = Arrow(start=elementos_dom_SOB[2].get_right(), end=elementos_codom_SOB[1].get_left(), color=BLACK)
        seta_5_25_SOB = Arrow(start=elementos_dom_SOB[3].get_right(), end=elementos_codom_SOB[2].get_left(), color=BLACK)

        self.play(Create(dom_elipse), Create(codom_elipse))
        self.play(Write(label_dom), Write(label_codom))
        self.play(FadeIn(elementos_dom_SOB), FadeIn(elementos_codom_SOB))
        self.wait()
        self.play(Create(seta_2_4_SOB), Create(seta_m2_4_SOB), Create(seta_3_9_SOB), Create(seta_5_25_SOB))
        self.wait()
        self.play(Create(ima_elipse), Write(label_ima))
        self.wait(3)

        self.play(FadeOut(dom_elipse, codom_elipse, ima_elipse, label_dom, label_codom, label_ima, elementos_dom_SOB, elementos_codom_SOB, seta_2_4_SOB, seta_m2_4_SOB, seta_3_9_SOB, seta_5_25_SOB, titulo))
        self.wait()

        #bijetora
        titulo = Tex(r"Função Bijetora", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.play(titulo.animate.to_corner(DOWN+LEFT, buff=0.2))
        self.wait()

        elementos_dom_BIJ = VGroup(
            Tex(r'2'), Tex(r'1'), Tex(r'3'), Tex(r'5')
        ).set_color(PURE_GREEN).scale(1.5).arrange(DOWN, buff=0.5).move_to(dom_elipse.get_center())

        elementos_codom_BIJ = VGroup(
            Tex(r'4'),
            Tex(r'1'), 
            Tex(r'9'), 
            Tex(r'25')
        ).scale(1.5).set_color(PURE_BLUE).arrange(DOWN, buff=0.5).move_to(codom_elipse.get_center())

        seta_2_4_BIJ = Arrow(start=elementos_dom_BIJ[0].get_right(), end=elementos_codom_BIJ[0].get_left(), color=BLACK)
        seta_1_1_BIJ = Arrow(start=elementos_dom_BIJ[1].get_right(), end=elementos_codom_BIJ[1].get_left(), color=BLACK)
        seta_3_9_BIJ = Arrow(start=elementos_dom_BIJ[2].get_right(), end=elementos_codom_BIJ[2].get_left(), color=BLACK)
        seta_5_25_BIJ = Arrow(start=elementos_dom_BIJ[3].get_right(), end=elementos_codom_BIJ[3].get_left(), color=BLACK)


    #resolver o problema de posicionamento da ima_elipse que nao está ficando centralizada nos elementos do contradom 
        ima_elipse = Ellipse(width=1.3, height=4.5, color=PURE_RED, fill_opacity=0).move_to(elementos_codom_BIJ[2].get_center())
        label_ima = Tex("Imagem", color=PURE_RED).scale(1.2).next_to(ima_elipse, RIGHT*2, buff=0.5)

        self.play(Create(dom_elipse), Create(codom_elipse))
        self.play(Write(label_dom), Write(label_codom))
        self.play(FadeIn(elementos_dom_BIJ), FadeIn(elementos_codom_BIJ))
        self.wait()
        self.play(Create(seta_2_4_BIJ), Create(seta_1_1_BIJ), Create(seta_3_9_BIJ), Create(seta_5_25_BIJ))
        self.wait()
        self.play(Create(ima_elipse), Write(label_ima))
        self.wait(3)

