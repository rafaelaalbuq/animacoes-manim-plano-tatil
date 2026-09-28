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

        titulo = Tex(r"Diagramas - Relações Entre Conjuntos").scale(1.2).move_to(ORIGIN)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))

        #exemplos diagramas 
        circulo_A = Circle(radius=2, color=PURE_GREEN, stroke_width=4).shift(LEFT*1.2)
        circulo_B = Circle(radius=2, color=PURE_RED, stroke_width=4).shift(RIGHT*1.2)
        circulo_C = Circle(radius=2, color=PINK, stroke_width=4).shift(DOWN*1)

        A_label = Tex(r"A").set_color(PURE_GREEN).scale(1.5).next_to(circulo_A, LEFT, buff=0.1)
        B_label = Tex(r"B").set_color(PURE_RED).scale(1.5).next_to(circulo_B, RIGHT, buff=0.1)
        C_label = Tex(r"C").set_color(PINK).scale(1.5).next_to(circulo_C, DOWN, buff=0.1)

        diagrama_1_grupo = VGroup(circulo_A, circulo_B, A_label, B_label)

        #intersecção

        inter_label_AB = Tex(r"$A \cap B$").set_color(BLACK).scale(2).to_edge(UP, buff=0.5)
        self.play(Write(inter_label_AB))
        self.wait()

        inter_AB = Intersection(circulo_A, circulo_B, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        self.play(Create(diagrama_1_grupo), FadeIn(inter_AB))
        self.wait(3)
       


        #uniao 

        uniao_label = Tex(r"$A \cup B$").set_color(BLACK).scale(2).to_edge(UP, buff=0.5)
        
        self.play(ReplacementTransform(inter_label_AB, uniao_label))
        self.wait()

        uniao_AB = Union(circulo_A, circulo_B, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        self.play(ReplacementTransform(inter_AB, uniao_AB))
        self.wait(3)
      



        
        #diferença a - b

        dif1_label = Tex(r"$A - B$").set_color(BLACK).scale(2).to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(uniao_label, dif1_label))
        self.wait()

        dif_AB = Difference(circulo_A, circulo_B, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        self.play(ReplacementTransform(uniao_AB, dif_AB))
        self.wait(3)
        


        #diferença b - a
        
        dif2_label = Tex(r"$B - A$").set_color(BLACK).scale(2).to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(dif1_label, dif2_label))
        self.wait()

        dif_BA = Difference(circulo_B, circulo_A, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        self.play(ReplacementTransform(dif_AB, dif_BA))
        self.wait(3)
        self.play(FadeOut(diagrama_1_grupo, dif_BA))

        #
        inter_ABC_label = Tex(r"$A \cap B \cap C$").set_color(BLACK).scale(2).to_edge(UP, buff=0.5)
        self.play(ReplacementTransform(dif2_label, inter_ABC_label))
        self.wait()

## EDITAR POSICOES E CORES

        circulo_A.move_to(UP*0.5+LEFT*1.2)
        circulo_B.move_to(UP*0.5+RIGHT*1.2)

        temp_inter_AB = Intersection(circulo_A, circulo_B)

        # 2. Agora criamos a interseção tripla usando essa temporária e o C
        inter_ABC = Intersection(temp_inter_AB, circulo_C, color=YELLOW, fill_opacity=0.7, stroke_opacity=0)

        self.play(Create(circulo_A), Create(circulo_B), Create(circulo_C), Write(A_label), Write(B_label), Write(C_label), FadeIn(inter_ABC))
        self.wait(3)
        self.play(FadeOut(circulo_A, circulo_B, circulo_C, A_label, B_label, C_label, inter_ABC, inter_ABC_label))
        self.wait()

        #exemplos com numeros

        circulo_A.move_to(LEFT*1.2)
        circulo_B.move_to(RIGHT*1.2)

        conj_A = Tex(r"A = \{1, 2, 3, 4\}").set_color(PURE_GREEN).scale(1.2).move_to(UP*2.5+LEFT*5)
        conj_A_label = Tex(r"A").set_color(PURE_GREEN).scale(1.2).next_to(circulo_A, LEFT*0.3, buff=0.5)
        
        conj_B = Tex(r"B = \{3, 4, 5, 6\}").set_color(PURE_RED).scale(1.2).next_to(conj_A, DOWN, buff=0.5)
        conj_B_label = Tex(r"B").set_color(PURE_RED).scale(1.2).next_to(circulo_B, RIGHT*0.3, buff=0.5)

        #inter AB

        inter_label_AB2 = Tex(r"$A \cap B$").set_color(BLACK).scale(2).to_corner(UP+LEFT, buff=0.2)
        inter_result = Tex(r"$A \cap B = \{3, 4\}$").set_color(BLACK).scale(1.2).to_corner(DOWN+LEFT, buff=0.2)


        inter_AB_grupo = VGroup(circulo_A, circulo_B, A_label, B_label)
        inter_AB_grupo.to_edge(RIGHT, buff=0.5)
        inter_AB_2 = Intersection(circulo_A, circulo_B, color=YELLOW, fill_opacity=1, stroke_opacity=0)

        self.play(Write(inter_label_AB2))
        self.wait()

        self.play(Write(conj_A), Write(conj_B), Create(circulo_A), Create(circulo_B), Write(A_label), Write(B_label), FadeIn(inter_AB_2))
        self.play(Write(inter_result))
        self.wait(3)
        self.play(FadeOut(conj_A, conj_B, circulo_A, circulo_B, A_label, B_label, inter_result, inter_label_AB2, inter_AB_2))
        self.wait()

        #uniao AB

        uniao_AB_2 = Union(circulo_A, circulo_B, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        uniao_label2 = Tex(r"$A \cup B$").set_color(BLACK).scale(2).to_corner(UP+LEFT, buff=0.2)
        uniao_result = Tex(r"$A \cup B = \{1, 2, 3, 4, 5, 6\}$").set_color(BLACK).scale(1.2).to_corner(DOWN+LEFT, buff=0.2)  
       
        self.play(Write(uniao_label2), Write(conj_A), Write(conj_B), Create(circulo_A), Create(circulo_B), Write(A_label), Write(B_label), FadeIn(uniao_AB_2))
        self.play(Write(uniao_result))
        self.wait(3)
        self.play(FadeOut(uniao_label2), FadeOut(conj_A), FadeOut(conj_B), FadeOut(circulo_A), FadeOut(circulo_B), FadeOut(A_label), FadeOut(B_label), FadeOut(uniao_result), FadeOut(uniao_AB_2))
        self.wait()

        #diferença AB

        dif_AB_2 = Difference(circulo_A, circulo_B, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        dif_label2 = Tex(r"$A - B$").set_color(BLACK).scale(2).to_corner(UP+LEFT, buff=0.2)
        dif_result = Tex(r"$A - B = \{1, 2\}$").set_color(BLACK).scale(1.2).to_corner(DOWN+LEFT, buff=0.2)

        self.play(Write(dif_label2), Write(conj_A), Write(conj_B), Create(circulo_A), Create(circulo_B), Write(A_label), Write(B_label), FadeIn(dif_AB_2))
        self.play(Write(dif_result))
        self.wait(3)
        self.play(FadeOut(dif_label2), FadeOut(conj_A), FadeOut(conj_B), FadeOut(circulo_A), FadeOut(circulo_B), FadeOut(A_label), FadeOut(B_label), FadeOut(dif_result), FadeOut(dif_AB_2))
        self.wait()

        #diferença BA

        dif_BA_2 = Difference(circulo_B, circulo_A, color=YELLOW, fill_opacity=1, stroke_opacity=0)
        dif_label3 = Tex(r"$B - A$").set_color(BLACK).scale(2).to_corner(UP+LEFT, buff=0.2)
        dif_result2 = Tex(r"$B - A = \{5, 6\}$").set_color(BLACK).scale(1.2).to_corner(DOWN+LEFT, buff=0.2)  

        self.play(Write(dif_label3), Write(conj_A), Write(conj_B), Create(circulo_A), Create(circulo_B), Write(A_label), Write(B_label), FadeIn(dif_BA_2))
        self.play(Write(dif_result2))
        self.wait(3)
        self.play(FadeOut(dif_label3), FadeOut(conj_A), FadeOut(conj_B), FadeOut(circulo_A), FadeOut(circulo_B), FadeOut(A_label), FadeOut(B_label), FadeOut(dif_result2), FadeOut(dif_BA_2))
        self.wait(3)
