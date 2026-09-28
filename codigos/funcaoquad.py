from manim import *

class quad(Scene):
    def construct(self):
        
        self.camera.background_color = WHITE
        
       
        # 1 Introdução da Função e Elementos
       
        
        titulo = Tex("Função Quadrática", color=BLACK, font_size=72)
        self.play(Write(titulo))
        self.wait(1)
        self.play(titulo.animate.to_edge(UP))

        formula = MathTex("f(x)", "=", "a", "x^2", "+", "b", "x", "+", "c", color=BLACK, font_size=72).shift(UP)
        self.play(Write(formula))
        self.wait(1)

        lbl_fx = Tex("$x =$ Variável Independente", color=BLACK, font_size=40).next_to(formula, DOWN, buff=0.8)
        lbl_a = Tex("$a =$ Coeficiente Quadrático", color=PURE_RED, font_size=40).next_to(lbl_fx, DOWN)
        lbl_b = Tex("$b =$ Coeficiente Linear", color=PURE_BLUE, font_size=40).next_to(lbl_a, DOWN)
        lbl_c = Tex("$c =$ Termo Independente (Corta o eixo y)", color=PURE_GREEN, font_size=40).next_to(lbl_b, DOWN)

        self.play(formula[3].animate.set_color(BLACK), formula[6].animate.set_color(BLACK), Write(lbl_fx))
        self.wait(1)
        self.play(formula[2].animate.set_color(PURE_RED), Write(lbl_a))
        self.wait(1)
        self.play(formula[5].animate.set_color(PURE_BLUE), Write(lbl_b))
        self.wait(1)
        self.play(formula[8].animate.set_color(PURE_GREEN), Write(lbl_c))
        self.wait(2)

        self.clear()

       
        # 2 A Tabela (x² - 2x - 3)
       
        
        titulo_tabela = Tex("Calculando: $f(x) = x^2 - 2x - 3$", color=BLACK, font_size=60).to_edge(UP)
        self.play(Write(titulo_tabela))

        tabela = MathTable(
            [
                ["-1", "(-1)^2 - 2(-1) - 3", "0"],
                ["0", "(0)^2 - 2(0) - 3", "-3"],
                ["1", "(1)^2 - 2(1) - 3", "-4"],
                ["2", "(2)^2 - 2(2) - 3", "-3"],
                ["3", "(3)^2 - 2(3) - 3", "0"]
            ],
            col_labels=[MathTex("x"), MathTex("x^2 - 2x - 3"), MathTex("f(x)")],
            include_outer_lines=True,
            line_config={"color": BLACK, "stroke_width": 4}
        ).scale(0.65).next_to(titulo_tabela, DOWN, buff=0.5)
        
        tabela.get_entries().set_color(BLACK)
        tabela.get_labels().set_color(PURE_BLUE)
        
        self.play(Create(tabela.get_horizontal_lines()), Create(tabela.get_vertical_lines()), Write(tabela.get_labels()))
        self.wait(1)

        for linha in tabela.get_rows()[1:]: 
            self.play(Write(linha), run_time=1.5)
            self.wait(0.5)

        self.wait(2)
        self.clear()

            
        # 3 Tabela + Gráfico
        
        
        titulo_grafico = MathTex("f(x) = x^2 - 2x - 3", color=BLACK, font_size=60).to_corner(UL)
        self.play(Write(titulo_grafico))

        tabela_resumo = MathTable(
            [["-1", "0"], ["0", "-3"], ["1", "-4"], ["2", "-3"], ["3", "0"]],
            col_labels=[MathTex("x"), MathTex("f(x)")],
            include_outer_lines=True,
            line_config={"color": BLACK, "stroke_width": 3}
        ).scale(0.6).next_to(titulo_grafico, DOWN, buff=0.5).to_edge(LEFT)
        tabela_resumo.get_entries().set_color(BLACK)
        tabela_resumo.get_labels().set_color(PURE_BLUE)

        grade = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-6, 6, 1],
            x_length=7,
            y_length=7,
            background_line_style={"stroke_color": GRAY, "stroke_width": 1, "stroke_opacity": 0.5},
            axis_config={"stroke_color": BLACK, "stroke_width": 2, "include_numbers": True}
        ).to_edge(RIGHT)
        grade.get_x_axis().numbers.set_color(BLACK)
        grade.get_y_axis().numbers.set_color(BLACK)

        self.play(FadeIn(tabela_resumo), FadeIn(grade))
        
        pontos_coords = [(-1, 0), (0, -3), (1, -4), (2, -3), (3, 0)]
        pontos = VGroup()

        for i, (x, y) in enumerate(pontos_coords):
            linha_tabela = tabela_resumo.get_rows()[i+1]
            box_destaque = SurroundingRectangle(linha_tabela, color=PURE_RED, stroke_width=3)
            self.play(Create(box_destaque), run_time=0.5)

            ponto = Dot(grade.c2p(x, y), color=PURE_RED, radius=0.1)
            pontos.add(ponto)
            
            if y != 0:
                rastro_x = DashedLine(start=grade.c2p(x, 0), end=grade.c2p(x, y), color=PURE_RED)
                rastro_y = DashedLine(start=grade.c2p(x, y), end=grade.c2p(0, y), color=PURE_BLUE)
                self.play(Create(rastro_x), run_time=0.5)
                self.play(FadeIn(ponto, scale=0.5))
                self.play(Create(rastro_y), run_time=0.5)
                self.wait(0.5)
                self.play(FadeOut(rastro_x), FadeOut(rastro_y), FadeOut(box_destaque), run_time=0.5)
            else:
                self.play(FadeIn(ponto, scale=0.5))
                self.wait(0.5)
                self.play(FadeOut(box_destaque), run_time=0.5)

        parabola = grade.plot(lambda x: x**2 - 2*x - 3, color=PURE_BLUE, stroke_width=6)
        self.play(Create(parabola), run_time=2)
        self.wait(2)
        self.clear()

            
        #4 Influência do 'a' e 'c'
            
        
        self.play(FadeIn(grade))
        parabola_atual = grade.plot(lambda x: x**2 - 2*x - 3, color=PURE_BLUE, stroke_width=6)
        self.play(Create(parabola_atual))

        txt_a_pos = Tex("Se $a > 0$: Concavidade para CIMA", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(Write(txt_a_pos))
        self.wait(2)

        parabola_neg = grade.plot(lambda x: -x**2 + 2*x + 3, color=PURE_RED, stroke_width=6)
        txt_a_neg = Tex("Se $a < 0$: Concavidade para BAIXO", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        
        self.play(Transform(parabola_atual, parabola_neg), Transform(txt_a_pos, txt_a_neg), run_time=2)
        self.wait(2)

        parabola_orig = grade.plot(lambda x: x**2 - 2*x - 3, color=PURE_BLUE, stroke_width=6)
        txt_c = Tex("Termo $c$: Onde corta o eixo y", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        
        self.play(Transform(parabola_atual, parabola_orig), Transform(txt_a_pos, txt_c))
        
        ponto_c = Dot(grade.c2p(0, -3), color=PURE_GREEN, radius=0.15)
        lbl_c_val = Tex("$c = -3$", color=PURE_GREEN, font_size=48).next_to(ponto_c, RIGHT).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(FadeIn(ponto_c), Write(lbl_c_val))
        self.wait(3)

        self.clear()

        
        #5 Raízes (Fórmula de Bhaskara)
        
        
        titulo_bhaskara = Tex("Encontrando as Raízes: $x^2 - 2x - 3 = 0$", color=BLACK, font_size=50).to_edge(UP)
        self.play(Write(titulo_bhaskara))

        delta_eq = MathTex("\\Delta = b^2 - 4ac", color=BLACK).shift(UP*1.5)
        delta_calc = MathTex("\\Delta = (-2)^2 - 4(1)(-3) = 16", color=BLACK).next_to(delta_eq, DOWN)
        
        bhaskara_eq = MathTex("x = \\frac{-b \\pm \\sqrt{\\Delta}}{2a}", color=BLACK).next_to(delta_calc, DOWN, buff=0.8)
        bhaskara_calc = MathTex("x = \\frac{2 \\pm 4}{2}", color=BLACK).next_to(bhaskara_eq, DOWN)
        
        raizes = MathTex("x_1 = 3 \\quad \\text{e} \\quad x_2 = -1", color=PURE_RED, font_size=56).next_to(bhaskara_calc, DOWN, buff=0.8)

        self.play(Write(delta_eq))
        self.wait(1)
        self.play(Write(delta_calc))
        self.wait(1)
        self.play(Write(bhaskara_eq))
        self.wait(1)
        self.play(Write(bhaskara_calc))
        self.wait(1)
        self.play(Write(raizes))
        self.wait(3)

        self.clear()

        
        # 6 O Vértice e a Simetria
           
        parabola_parte6 = grade.plot(lambda x: x**2 - 2*x - 3, color=PURE_BLUE, stroke_width=6)
        self.play(FadeIn(grade), FadeIn(parabola_parte6))
        
        # Caso a > 0 (Mínimo)
        txt_vertice = Tex("O Vértice (Ponto Mínimo) $a > 0$", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(Write(txt_vertice))

        r1 = Dot(grade.c2p(-1, 0), color=PURE_RED, radius=0.1)
        r2 = Dot(grade.c2p(3, 0), color=PURE_RED, radius=0.1)
        lbl_raizes = Tex("Raízes", color=PURE_RED, font_size=36).next_to(r2, UR).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(FadeIn(r1, r2), Write(lbl_raizes))

        eixo_simetria = DashedLine(start=grade.c2p(1, 6), end=grade.c2p(1, -6), color=GRAY, stroke_width=3)
        lbl_simetria = Tex("Simetria ($X_v = 1$)", color=BLACK, font_size=36).next_to(eixo_simetria, RIGHT).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(Create(eixo_simetria), Write(lbl_simetria))
        
        vertice = Dot(grade.c2p(1, -4), color=PURE_BLUE, radius=0.15)
        lbl_vertice = MathTex("V(1, -4)", color=PURE_BLUE, font_size=40).next_to(vertice, DOWN).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(FadeIn(vertice, scale=0.5), Write(lbl_vertice))
        self.wait(3)

        # Caso a < 0 (Máximo)
        txt_vertice_max = Tex("O Vértice (Ponto Máximo) $a < 0$", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        parabola_invertida = grade.plot(lambda x: -x**2 + 2*x + 3, color=PURE_RED, stroke_width=6)
        vertice_max = Dot(grade.c2p(1, 4), color=PURE_RED, radius=0.15)
        lbl_vertice_max = MathTex("V(1, 4)", color=PURE_RED, font_size=40).next_to(vertice_max, UP).add_background_rectangle(color=WHITE, opacity=0.9)

        self.play(
            Transform(txt_vertice, txt_vertice_max),
            Transform(parabola_parte6, parabola_invertida),
            Transform(vertice, vertice_max),
            Transform(lbl_vertice, lbl_vertice_max)
        )
        self.wait(3)

        self.clear()

        
        # 7 Estudo dos Sinais
      
        
        parabola_parte7 = grade.plot(lambda x: x**2 - 2*x - 3, color=PURE_BLUE, stroke_width=6)
        self.play(FadeIn(grade), FadeIn(parabola_parte7), FadeIn(r1, r2))

        # CASO 1: a > 0
        txt_sinal = Tex("Estudo do Sinal ($a > 0$)", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        self.play(Write(txt_sinal))

        sinal_neg = Tex("$-$", color=PURE_RED, font_size=90).move_to(grade.c2p(1, -2)).add_background_rectangle(color=WHITE, opacity=0.7)
        sinal_pos1 = Tex("$+$", color=PURE_GREEN, font_size=90).move_to(grade.c2p(-3, 3)).add_background_rectangle(color=WHITE, opacity=0.7)
        sinal_pos2 = Tex("$+$", color=PURE_GREEN, font_size=90).move_to(grade.c2p(4, 3)).add_background_rectangle(color=WHITE, opacity=0.7)

        txt_negativo = Tex("Entre as raízes: Negativo ($y < 0$)", color=PURE_RED, font_size=40).to_edge(DOWN).add_background_rectangle(color=WHITE, opacity=0.9).next_to(txt_sinal, DOWN, buff=0.5)
        txt_positivo = Tex("Fora das raízes: Positivo ($y > 0$)", color=PURE_GREEN, font_size=40).to_edge(UP).add_background_rectangle(color=WHITE, opacity=0.9).next_to(txt_negativo, DOWN, buff=0.5)

        self.play(Write(txt_negativo), FadeIn(sinal_neg, scale=0.5))
        self.wait(2)
        
        self.play(Write(txt_positivo), FadeIn(sinal_pos1, scale=0.5), FadeIn(sinal_pos2, scale=0.5))
        self.wait(3)

        # CASO 2: a < 0
        txt_sinal_inv = Tex("Estudo do Sinal ($a < 0$)", color=BLACK).to_corner(UL).add_background_rectangle(color=WHITE, opacity=0.9)
        parabola_parte7_inv = grade.plot(lambda x: -x**2 + 2*x + 3, color=PURE_RED, stroke_width=6)
        
        sinal_pos_meio = Tex("$+$", color=PURE_GREEN, font_size=90).move_to(grade.c2p(1, 2)).add_background_rectangle(color=WHITE, opacity=0.7)
        sinal_neg_esq = Tex("$-$", color=PURE_RED, font_size=90).move_to(grade.c2p(-3, -3)).add_background_rectangle(color=WHITE, opacity=0.7)
        sinal_neg_dir = Tex("$-$", color=PURE_RED, font_size=90).move_to(grade.c2p(4, -3)).add_background_rectangle(color=WHITE, opacity=0.7)

        txt_positivo_inv = Tex("Entre as raízes: Positivo ($y > 0$)", color=PURE_GREEN, font_size=40).to_edge(DOWN).add_background_rectangle(color=WHITE, opacity=0.9).next_to(txt_sinal_inv, DOWN, buff=0.5)
        txt_negativo_inv = Tex("Fora das raízes: Negativo ($y < 0$)", color=PURE_RED, font_size=40).to_edge(UP).add_background_rectangle(color=WHITE, opacity=0.9).next_to(txt_positivo_inv, DOWN, buff=0.5)

        # Limpando sinais antigos e transformando a parábola
        self.play(
            FadeOut(sinal_neg), FadeOut(sinal_pos1), FadeOut(sinal_pos2),
            FadeOut(txt_negativo), FadeOut(txt_positivo),
            Transform(txt_sinal, txt_sinal_inv),
            Transform(parabola_parte7, parabola_parte7_inv)
        )

        # Mostrando os novos sinais
        self.play(Write(txt_positivo_inv), FadeIn(sinal_pos_meio, scale=0.5))
        self.wait(2)

        self.play(Write(txt_negativo_inv), FadeIn(sinal_neg_esq, scale=0.5), FadeIn(sinal_neg_dir, scale=0.5))
        self.wait(3)

        # Encerramento
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(1)