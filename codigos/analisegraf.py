from manim import *
import numpy as np

class plano(MovingCameraScene):
    def construct(self):
        # 1 Configuração de Fundo e Logo
        cordefundo = ManimColor("#D5D5DD")
        self.camera.background_color = cordefundo

        try:
            img = ImageMobject('logounivasfbranca').scale(0.2)
            img.to_corner(DR, buff=0.1)
            self.add(img)
        except:
            print('LOGO NAO ENCONTRADA')

        # 2 Título Inicial 
        titulo = Tex(r"Análise de Gráficos", color=BLACK).scale(1.5)
        self.play(Write(titulo))
        self.wait()
        self.play(FadeOut(titulo))


        self.camera.frame.save_state()
        self.camera.frame.set(width=22) 


         # 3 Construção dos Eixos
        reta_X = NumberLine(x_range=[-11, 11], color=GRAY_E, stroke_width=2)
        reta_Y = NumberLine(x_range=[-11, 11], color=GRAY_E, stroke_width=2)
        
        self.play(Create(reta_X), Create(reta_Y))
        self.play(reta_Y.animate.rotate(90 * DEGREES, about_point=ORIGIN))
        self.wait(0.5)
        
        # 4 Configuração da Grade (NumberPlane)
     
        grade = NumberPlane(
            x_range=[-11, 11, 1],
            y_range=[-11, 11, 1],
            background_line_style={
                "stroke_color": GRAY_A,
                "stroke_width": 1,
                "stroke_opacity": 0.5
            },
            axis_config={
                "stroke_color": GRAY_B,
                "stroke_width": 2,
                "include_numbers": False,
                "include_ticks": True
            }
        ).set_color(BLACK) 

   
        self.play(FadeIn(grade))
        self.remove(reta_X, reta_Y) 
        self.wait()


#sinal da funcao
        sinal_tit = Tex(r'Sinal da Função', color=PURE_RED).scale(1.5)

        sinal_tit.move_to([-8, 5.5, 0])
        
        self.play(Write(sinal_tit))
        self.wait()

        # 1 Definindo a função matemática (polinômio de grau 5)
        def func(x):
            return 0.05 * (x + 3) * (x + 1) * (x - 1) * (x - 3) * (x - 5)

        # 2. Criando o gráfico atrelado à "grade"
        
        grafico = grade.plot(func, color=BLACK, x_range=[-4.5, 6])
        
        # 3 Criando os preenchimentos para o Estudo do Sinal
        # Áreas Positivas (Azul)
        area_pos1 = grade.get_area(grafico, x_range=[-3, -1], color=GREEN, opacity=0.3)
        area_pos2 = grade.get_area(grafico, x_range=[1, 3], color=GREEN, opacity=0.3)
        area_pos3 = grade.get_area(grafico, x_range=[5, 6], color=GREEN, opacity=0.3)
        
        # Áreas Negativas (Vermelho)
        area_neg1 = grade.get_area(grafico, x_range=[-4.5, -3], color=RED, opacity=0.3)
        area_neg2 = grade.get_area(grafico, x_range=[-1, 1], color=RED, opacity=0.3)
        area_neg3 = grade.get_area(grafico, x_range=[3, 5], color=RED, opacity=0.3)

        # 4 Animando o surgimento da curva
        self.play(Create(grafico), run_time=3)
        self.wait()
        
        # 5.Animando o surgimento dos sinais
        self.play(
            FadeIn(area_pos1, area_pos2, area_pos3),
            FadeIn(area_neg1, area_neg2, area_neg3)
        )
        self.wait(3)

        #fadeout de sinal da funcao
        self.play(FadeOut(sinal_tit), FadeOut(grafico), FadeOut(area_pos1), FadeOut(area_pos2), FadeOut(area_pos3), FadeOut(area_neg1), FadeOut(area_neg2), FadeOut(area_neg3))
        self.wait()



#crescimento -- decrescimento


        def func(x):
            return (x**3) / 3 - 4 * x

        # 3 Dividindo a Curva nas 3 zonas (Crescente -> Decrescente -> Crescente)
        grafico_crescente1 = grade.plot(func, x_range=[-4.5, -2], color=GREEN)
        grafico_decrescente = grade.plot(func, x_range=[-2, 2], color=RED)
        grafico_crescente2 = grade.plot(func, x_range=[2, 4.5], color=GREEN)

        
        ponto = Dot(grade.c2p(-4.5, func(-4.5)), color=GREEN, radius=0.15)

        
        def update_dot(d):
            x = grade.p2c(d.get_center())[0] 
            if x <= -1.95 or x >= 1.95:      
                d.set_color(GREEN)
            else:
                d.set_color(RED)
        ponto.add_updater(update_dot)

        
        linha_tracejada = always_redraw(
            lambda: DashedLine(
                start=ponto.get_center(),
                end=grade.c2p(grade.p2c(ponto.get_center())[0], 0), # Coordenada [X, 0]
                color=ponto.get_color(),
                stroke_width=3
            )
        )

        
        texto_estado = Tex("Função Crescente", color=PURE_GREEN).scale(1.5)
        texto_estado.move_to([-7, 5.5, 0])

       
        def update_text(text):
            x = grade.p2c(ponto.get_center())[0]
            if x <= -1.95 or x >= 1.95:
               
                text.become(Tex("Função Crescente", color=PURE_GREEN).scale(1.5).move_to([-7, 5.5, 0]))
            else:
                text.become(Tex("Função Decrescente", color=PURE_RED).scale(1.5).move_to([-7, 5.5, 0]))
        texto_estado.add_updater(update_text)

        # Colocando os elementos responsivos na tela antes de rodar o movimento
        self.add(texto_estado)
        self.add(ponto, linha_tracejada)

        
        self.play(
            Create(grafico_crescente1, rate_func=linear),
            MoveAlongPath(ponto, grafico_crescente1, rate_func=linear),
            run_time=2.5
        )
        self.play(
            Create(grafico_decrescente, rate_func=linear),
            MoveAlongPath(ponto, grafico_decrescente, rate_func=linear),
            run_time=4 # Tempo maior porque esse trecho do meio é mais longo
        )
        self.play(
            Create(grafico_crescente2, rate_func=linear),
            MoveAlongPath(ponto, grafico_crescente2, rate_func=linear),
            run_time=2.5
        )

        self.wait(2)

        #fadeout de crescimento e decrescimento
        self.play(FadeOut(texto_estado), FadeOut(ponto), FadeOut(linha_tracejada), FadeOut(grafico_crescente1), FadeOut(grafico_decrescente), FadeOut(grafico_crescente2))
        self.wait()



#maximos --- minimos


        maxmin_tit = Tex(r'Máximos e Mínimos', color=YELLOW).scale(1.5).move_to([-7.5, 5.5, 0])
        self.add(maxmin_tit)


        def func(x):
            return (x**3) / 3 - 4 * x

        grafico = grade.plot(func, x_range=[-4.5, 4.5], color=BLACK, stroke_width=3)
        self.play(Create(grafico), run_time=2)
        self.wait(0.5)

        # 3 MÁXIMO LOCAL (O Pico)
        x_max = -2
        y_max = func(x_max)
        coord_max = grade.c2p(x_max, y_max)
        
        ponto_max = Dot(coord_max, color=BLUE, radius=0.2)
        #texto_max = Tex("Máximo Local", color=BLUE).scale(1.2).next_to(ponto_max, UL)
        
        # Linha horizontal no topo (mostrando que a curva parou de subir)
        tangente_max = Line(
            grade.c2p(x_max - 1.5, y_max), 
            grade.c2p(x_max + 1.5, y_max), 
            color=BLUE, stroke_width=2
        )

        # Linhas tracejadas indo para os eixos X e Y
        linhas_eixo_max = VGroup(
            DashedLine(coord_max, grade.c2p(x_max, 0), color=GRAY_D),
            DashedLine(coord_max, grade.c2p(0, y_max), color=GRAY_D)
        )

        # Animação do Máximo
        self.play(FadeIn(ponto_max, scale=0.5))
        self.play(Create(tangente_max))
        self.play(Create(linhas_eixo_max))
        self.wait(1.5)

        # 4 MÍNIMO LOCAL
        x_min = 2
        y_min = func(x_min)
        coord_min = grade.c2p(x_min, y_min)
        
        ponto_min = Dot(coord_min, color=PURE_RED, radius=0.2)
        #texto_min = Tex("Mínimo Local", color=PURE_RED).scale(1.2).next_to(ponto_min, DL)
        
        tangente_min = Line(
            grade.c2p(x_min - 1.5, y_min), 
            grade.c2p(x_min + 1.5, y_min), 
            color=PURE_RED, stroke_width=2
        )

        linhas_eixo_min = VGroup(
            DashedLine(coord_min, grade.c2p(x_min, 0), color=GRAY_D),
            DashedLine(coord_min, grade.c2p(0, y_min), color=GRAY_D)
        )

        # Animação do Mínimo
        self.play(FadeIn(ponto_min, scale=0.5))
        self.play(Create(tangente_min))
        self.play(Create(linhas_eixo_min))
        
        self.wait(3)

        #fadeout de maximos e minimos
        self.play(FadeOut(ponto_max), FadeOut(tangente_max), FadeOut(linhas_eixo_max), FadeOut(ponto_min), FadeOut(tangente_min), FadeOut(linhas_eixo_min), FadeOut(grafico), FadeOut(maxmin_tit))




#simetria 


         #par
        titulo_par = Tex("Função Par:\n $f(x) = f(-x)$", color=PURE_GREEN).scale(1.5).move_to([-6, 5.5, 0])
        func_par = lambda x: 0.3 * x**2 - 4 # Parábola
        graf_par = grade.plot(func_par, color=BLACK, stroke_width=4)
        
        self.play(Write(titulo_par), Create(graf_par))
        
        # O Ponto no lado positivo (x = 4)
        px1, py1 = 4, func_par(4)
        ponto_dir = Dot(grade.c2p(px1, py1), color=YELLOW, radius=0.15)
        linha_y_dir = DashedLine(grade.c2p(px1, py1), grade.c2p(px1, 0), color=GRAY)
        
        # O Ponto refletido no lado negativo (x = -4)
        px2, py2 = -4, func_par(-4)
        ponto_esq = Dot(grade.c2p(px2, py2), color=YELLOW, radius=0.15)
        linha_y_esq = DashedLine(grade.c2p(px2, py2), grade.c2p(px2, 0), color=GRAY)
        
        linha_espelho = DashedLine(grade.c2p(px1, py1), grade.c2p(px2, py2), color=WHITE, stroke_width=3)
        
        self.play(FadeIn(ponto_dir), Create(linha_y_dir))
        self.wait(0.5)
        # Anima a cópia viajando para o outro lado para provar a mesma altura
        self.play(TransformFromCopy(ponto_dir, ponto_esq), Create(linha_espelho), Create(linha_y_esq))
        self.wait(2)
        
        # Limpando a tela para a próxima cena
        self.play(FadeOut(titulo_par, graf_par, ponto_dir, ponto_esq, linha_y_dir, linha_y_esq, linha_espelho))

    #impar
        titulo_impar = Tex("Função Ímpar: $f(-x) = -f(x)$", color=PURE_RED).scale(1.5).move_to([-6, 5.5, 0])
        func_impar = lambda x: 0.05 * x**3 # Cúbica ("S")
        graf_impar = grade.plot(func_impar, color=BLACK, stroke_width=4)
        
        self.play(Write(titulo_impar), Create(graf_impar))

        # Ponto positivo (x = 4)
        px1_i, py1_i = 4, func_impar(4)
        ponto_dir_i = Dot(grade.c2p(px1_i, py1_i), color=YELLOW, radius=0.15)
        
        # Ponto refletido na ORIGEM (x = -4, y = -y)
        px2_i, py2_i = -4, func_impar(-4)
        ponto_esq_i = Dot(grade.c2p(px2_i, py2_i), color=YELLOW, radius=0.15)
        
        # A linha cruzando a origem (0,0)
        linha_origem = DashedLine(grade.c2p(px1_i, py1_i), grade.c2p(px2_i, py2_i), color=WHITE, stroke_width=3)
        
        self.play(FadeIn(ponto_dir_i))
        self.wait(0.5)
        
        self.play(Create(linha_origem))
        self.play(FadeIn(ponto_esq_i))
        self.wait(2)

        self.play(FadeOut(titulo_impar, graf_impar, ponto_dir_i, ponto_esq_i, linha_origem))

    #assimétrica
        titulo_assi = Tex("Assimétrica", color=PURE_RED).scale(1.5).move_to([-9, 5.5, 0])
        func_assi = lambda x: 1.5 * x + 3 # Reta deslocada (ax + b)
        graf_assi = grade.plot(func_assi, color=RED_E, stroke_width=4)
        
        self.play(Write(titulo_assi), Create(graf_assi))

        # Escolhemos x = 1
        px1_a, py1_a = 1, func_assi(1)
        ponto_dir_a = Dot(grade.c2p(px1_a, py1_a), color=YELLOW, radius=0.15)
        
        # Tentamos espelhar no eixo y (x = -1, y = igual)
        ponto_falso_par = Dot(grade.c2p(-1, py1_a), color=GRAY, radius=0.15)
        linha_falha_par = DashedLine(grade.c2p(px1_a, py1_a), grade.c2p(-1, py1_a), color=GRAY)
        
        # Xis vermelho para mostrar que o ponto caiu fora da linha
        xis = Cross(ponto_falso_par, stroke_color=PURE_RED, scale_factor=0.3)
        
        self.play(FadeIn(ponto_dir_a))
        self.play(Create(linha_falha_par), FadeIn(ponto_falso_par))
        self.play(Create(xis)) # Mostra que f(-x) não é igual a f(x)
        self.wait(5)

        #fadeout geral - limpar tudo
        self.play(FadeOut(titulo_assi, graf_assi, ponto_dir_a, ponto_falso_par, linha_falha_par, xis))
        #fadeout plano
        self.play(FadeOut(grade))
        self.wait()



        
