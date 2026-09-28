from manim import*

class conjuntos(Scene):
    def construct(self):
        
    
        self.camera.background_color = WHITE

        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff = 0.1)
            self.add(img)
        except:
            print('LOGO NAO ENCONTRADA')

        # 1 Definição das formas
        A = Ellipse(width=3, height=6, color=PURE_RED).shift(LEFT*2)    
        B = Ellipse(width=3, height=6, color=PURE_GREEN).shift(RIGHT*2)

        # 2 Rótulos
        A_label = Tex(r'A').set_color(PURE_RED).scale(1.2).next_to(A, UP, buff=0.2)
        B_label = Tex(r'B').set_color(PURE_GREEN).scale(1.2).next_to(B, UP, buff=0.2)

        # 3 Elementos
        
        grupoA = VGroup(
            Tex(r'1'), Tex(r'2'), Tex(r'3'), Tex(r'4')
        ).set_color(BLACK).scale(1.5).arrange(DOWN, buff=0.5)

        grupoB = VGroup(
            Tex(r'4'), Tex(r'5'), Tex(r'6')
        ).set_color(BLACK).scale(1.5).arrange(DOWN, buff=0.5)

        
        grupoA.move_to(A.get_center())
        grupoB.move_to(B.get_center())

        # 5 Animação
        
        self.play(
            Create(A), Create(B), 
            Write(A_label), Write(B_label)
        )
        self.play(FadeIn(grupoA), FadeIn(grupoB))
        self.wait(2)

        # União
        uniao_txt = Tex(r'$A \cup B$').set_color(PURE_BLUE).scale(2).to_edge(UP, buff=0.2)
        conj_uniao = Ellipse(width=4, height=6, color=PURE_BLUE).move_to(DOWN*0.5)
        
        # Elementos da união
        elementos_uniao = VGroup(
            Tex(r'1'), Tex(r'2'), Tex(r'3'), 
            Tex(r'4'), Tex(r'5'), Tex(r'6')
        ).set_color(BLACK).scale(1.5).arrange(DOWN, buff=0.4)
        
        elementos_uniao.move_to(conj_uniao.get_center())

        self.play(FadeOut(A, B, A_label, B_label, grupoA, grupoB))
        self.wait()
        self.play(Write(uniao_txt))
        self.play( Create(conj_uniao), FadeIn(elementos_uniao))
        self.wait(2)

        self.play(FadeOut(uniao_txt, conj_uniao, elementos_uniao))
        self.wait()
        

        #interseção
        
        intersecao_txt = Tex(r'$A \cap B$').set_color(PURE_BLUE).scale(2).to_edge(UP, buff=0.2)
        conj_intersecao = Ellipse(width=2, height=4, color=PURE_BLUE).move_to(ORIGIN)
       
        elementos_intersecao = VGroup(
            Tex(r'4')
        ).set_color(BLACK).scale(1.5).arrange(DOWN, buff=0.4)
        elementos_intersecao.move_to(conj_intersecao.get_center())

        self.play(Write(intersecao_txt))
        self.play(Create(conj_intersecao), FadeIn(elementos_intersecao))
        self.wait(2)
        self.play(FadeOut(intersecao_txt, conj_intersecao, elementos_intersecao))
        self.wait()

        #mais exemplos - subconj

        conj1_elipse = Ellipse(width=2, height=4.5, color=PURE_RED).shift(LEFT*1)
        conj1 = Tex(r'A = \{5, 13, 3.14\}').set_color(PURE_RED).scale(1.2).move_to(LEFT*4.5)
        conj1_label = Tex(r'A').set_color(PURE_RED).scale(1.2).next_to(conj1_elipse, LEFT*0.3, buff=0.5)
        conj1_elementos = VGroup(
            Tex(r'5').set_color(BLACK).scale(1.5),
            Tex(r'13').set_color(BLACK).scale(1.5),
            Tex(r'3.14').set_color(BLACK).scale(1.5)
        ).set_color(BLACK).arrange(DOWN, buff=0.8).move_to(conj1_elipse.get_center())
        conj1_grupo = VGroup(conj1_elipse, conj1_label, conj1_elementos)

        conj2_quadrado = Square(side_length=5.5, color=PURE_GREEN).shift(ORIGIN)
        conj2 = Tex(r'B = \{5, 13, 3.14, 1, 99\}').set_color(PURE_GREEN).scale(1.2).next_to(conj1, RIGHT, buff=0.3)
        conj2_label = Tex(r'B').set_color(PURE_GREEN).scale(1.2).next_to(conj2_quadrado, LEFT, buff=0.5)
        conj2_elementos = VGroup(
            #Tex(r'5').set_color(PURE_GREEN).scale(1.5),
            #Tex(r'13').set_color(PURE_GREEN).scale(1.5),
            #Tex(r'3.14').set_color(PURE_GREEN).scale(1.5),
            Tex(r'1').set_color(BLACK).scale(1.5),
            Tex(r'99').set_color(BLACK).scale(1.5)     
        ).set_color(BLACK).arrange_in_grid(rows=2, cols=3, buff=0.8).next_to(conj2_quadrado.get_right(), LEFT, buff=0.8)
        conj2_grupo = VGroup(conj2_quadrado, conj2_label, conj2_elementos)  


        conj3 = Tex(r'C = \{7\}').set_color(PINK).scale(1.2).next_to(conj2, RIGHT, buff=0.3)

        conj3_elipse = Ellipse(width=1.5, height=3, color=PINK).next_to(conj2_quadrado, RIGHT, buff=0.5)
        conj3_label = Tex(r'C').set_color(PINK).scale(1.2).next_to(conj3_elipse, UP, buff=0.5)
        conj3_elementos = VGroup(
            Tex(r'7').set_color(BLACK).scale(1.5)
        ).set_color(BLACK).arrange(DOWN, buff=0.8).move_to(conj3_elipse.get_center())
        conj3_grupo = VGroup(conj3_elipse, conj3_label, conj3_elementos)


        self.play(Write(conj1), Write(conj2), Write(conj3))
        self.wait()
        self.play(FadeOut(conj1, conj2, conj3))
        self.wait(2)
        self.play(Create(conj1_elipse), FadeIn(conj1_label), FadeIn(conj1_elementos))
        self.wait()
        self.play(Create(conj2_quadrado), FadeIn(conj2_label), FadeIn(conj2_elementos))
        self.wait()
        self.play(Create(conj3_elipse), FadeIn(conj3_label), FadeIn(conj3_elementos))
        self.wait(3)
        self.play(conj1_grupo.animate.shift(LEFT*3), conj2_grupo.animate.shift(LEFT*3), conj3_grupo.animate.shift(LEFT*3))
        self.wait(2)

        contido1_2 = Tex(r'$A \subset B$').set_color(PURE_BLUE).scale(2.5).next_to(conj3_elipse, RIGHT, buff=0.5)

        naocontido = Tex(r'$C \not\subset B$').set_color(PURE_BLUE).scale(2.5).next_to(conj3_elipse, RIGHT, buff=0.5)

        self.play(Write(contido1_2))
        self.wait(3)
        self.play(ReplacementTransform(contido1_2, naocontido))
        self.wait(3)

        self.play(FadeOut(conj1_grupo, conj2_grupo, conj3_grupo, naocontido))
        self.wait()

        
       


        
            
        



        

