import tkinter as tk
from tkinter import messagebox


def menu():
    root = tk.Tk()
    root.title("PetroCalc")

    def choose():
        def back():
            select.withdraw()
            root.deiconify()

        def window1():
            select.withdraw()
            window_1 = tk.Tk()
            window_1.title("PetroCalc")

            title2_label = tk.Label(window_1, text="Adhesion Tension", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title2_label.grid(row=0, column=0)

            oso_label = tk.Label(window_1, text="Enter value of Interfacial Tension "
                                                "between the solid and oil (dyn/cm):", font=("Satoshi", 10, "bold"))
            oso_label.grid(row=1, column=0)

            osw_label = tk.Label(window_1, text="Enter value of Interfacial Tension "
                                                "between the solid and water (dyn/cm):", font=("Satoshi", 10, "bold"))
            osw_label.grid(row=2, column=0)

            def back1():
                window_1.withdraw()
                select.deiconify()

            def compute_adh():
                a = float(oso.get())
                b = float(osw.get())
                adh_tension = a - b

                adh_label = tk.Label(window_1, text=f"The computed Adhesion Tension "
                                                    f"is: {round(adh_tension, 2)} dyn/"
                                                    f"cm.", font=("Satoshi", 10, "bold"))
                adh_label.grid(row=6, column=0)

            oso = tk.Entry(window_1)
            oso.grid(row=1, column=2)

            osw = tk.Entry(window_1)
            osw.grid(row=2, column=2)

            compute = tk.Button(window_1, text="Compute", font="Satoshi", command=compute_adh)
            compute.grid(row=7, column=2)

            back_button1 = tk.Button(window_1, text="Back", font="Satoshi", command=back1)
            back_button1.grid(row=7, column=0)

            window_1.mainloop()

        def window2():
            select.withdraw()
            window_2 = tk.Tk()
            window_2.title("PetroCalc")

            title3_label = tk.Label(window_2, text="Amott-Harvey Wetability "
                                                   "Index", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title3_label.grid(row=0, column=0)

            io_label = tk.Label(window_2, text="Enter value of Oil Spontaneous Imbibition Ratio "
                                               "(dyn/cm):", font=("Satoshi", 10, "bold"))
            io_label.grid(row=1, column=0)

            iw_label = tk.Label(window_2, text="Enter value of Water Spontaneous Imbibition Ratio "
                                               "(dyn/cm):", font=("Satoshi", 10, "bold"))
            iw_label.grid(row=2, column=0)

            def back2():
                window_2.withdraw()
                select.deiconify()

            def compute_ahi():
                c = float(io.get())
                d = float(iw.get())
                ah_index = c - d

                ah_label = tk.Label(window_2, text=f"The Amott-Harvey Wetability Index is: {round(ah_index, 2)} "
                                                   f"(dimensionless).", font=("Satoshi", 10, "bold"))
                ah_label.grid(row=3, column=0)

            io = tk.Entry(window_2)
            io.grid(row=1, column=1)

            iw = tk.Entry(window_2)
            iw.grid(row=2, column=1)

            compute = tk.Button(window_2, text="Compute", font="Satoshi", command=compute_ahi)
            compute.grid(row=4, column=1)

            back_button2 = tk.Button(window_2, text="Back", font="Satoshi", command=back2)
            back_button2.grid(row=4, column=0)

            window_2.mainloop()

        def window3():
            select.withdraw()
            window_3 = tk.Tk()
            window_3.title("PetroCalc")

            title4_label = tk.Label(window_3, text="Apparent Facial Tension (De Nouy Ring "
                                                   "Method)", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title4_label.grid(row=0, column=0)

            m_weight_label = tk.Label(window_3, text="Enter value of measured weight "
                                                     "(in grams(g)):", font=("Satoshi", 10, "bold"))
            m_weight_label.grid(row=1, column=0)

            p_ring_label = tk.Label(window_3, text="Enter value of the perimeter of the ring "
                                                   "(in centimeter(cm)):", font=("Satoshi", 10, "bold"))
            p_ring_label.grid(row=2, column=0)

            def back3():
                window_3.withdraw()
                select.deiconify()

            def compute_aft():
                gravity = 980
                e = float(m_weight.get())
                f = float(p_ring.get())
                app_facial_tension = (e * gravity) / (2 * f)

                aft_label = tk.Label(window_3, text=f"The Apparent Facial Tension (De Nouy Ring Method) "
                                                    f"is: {round(app_facial_tension, 2)} "
                                                    f"dyn/cm.", font=("Satoshi", 10, "bold"))
                aft_label.grid(row=3, column=0)

            m_weight = tk.Entry(window_3)
            m_weight.grid(row=1, column=1)

            p_ring = tk.Entry(window_3)
            p_ring.grid(row=2, column=1)

            compute = tk.Button(window_3, text="Compute", font="Satoshi", command=compute_aft)
            compute.grid(row=4, column=1)

            back_button3 = tk.Button(window_3, text="Back", font="Satoshi", command=back3)
            back_button3.grid(row=4, column=0)

            window_3.mainloop()

        def window4():
            select.withdraw()
            window_4 = tk.Tk()
            window_4.title("PetroCalc")

            title5_label = tk.Label(window_4, text="Average Gas Solubility", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title5_label.grid(row=0, column=0)

            solubility_p1_label = tk.Label(window_4, text="Enter value of Solubility at p1 "
                                                          "(SCF/STB):", font=("Satoshi", 10, "bold"))
            solubility_p1_label.grid(row=1, column=0)

            solubility_p2_label = tk.Label(window_4, text="Enter value of Solubility at p2 "
                                                          "(SCF/STB):", font=("Satoshi", 10, "bold"))
            solubility_p2_label.grid(row=2, column=0)

            pressure1_label = tk.Label(window_4, text="Enter value of Pressure 1 (psi):", font=("Satoshi", 10, "bold"))
            pressure1_label.grid(row=3, column=0)

            pressure2_label = tk.Label(window_4, text="Enter value of Pressure 2 (psi):", font=("Satoshi", 10, "bold"))
            pressure2_label.grid(row=4, column=0)

            def back4():
                window_4.withdraw()
                select.deiconify()

            def compute_gs():
                g = float(solubility_p1.get())
                h = float(solubility_p2.get())
                i = float(pressure1.get())
                j = float(pressure2.get())
                avg_gs = (g - h) / (i - j)

                aft_label = tk.Label(window_4, text=f"The computed Average Gas Solubility is: {round(avg_gs, 2)} SCF"
                                                    f"/STB/psi.", font=("Satoshi", 10, "bold"))
                aft_label.grid(row=5, column=0)

            solubility_p1 = tk.Entry(window_4)
            solubility_p1.grid(row=1, column=1)

            solubility_p2 = tk.Entry(window_4)
            solubility_p2.grid(row=2, column=1)

            pressure1 = tk.Entry(window_4)
            pressure1.grid(row=3, column=1)

            pressure2 = tk.Entry(window_4)
            pressure2.grid(row=4, column=1)

            compute = tk.Button(window_4, text="Compute", font="Satoshi", command=compute_gs)
            compute.grid(row=6, column=1)

            back_button4 = tk.Button(window_4, text="Back", font="Satoshi", command=back4)
            back_button4.grid(row=6, column=0)

            window_4.mainloop()

        def window5():
            select.withdraw()
            window_5 = tk.Tk()
            window_5.title("PetroCalc")

            title6_label = tk.Label(window_5, text="Facial Tension (De Nouy Ring "
                                                   "Method)", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title6_label.grid(row=0, column=0)

            c_factor_label = tk.Label(window_5, text="Enter value of Correction Factor "
                                                     "(dimensionless):", font=("Satoshi", 10, "bold"))
            c_factor_label.grid(row=1, column=0)

            app_facial_tension_label = tk.Label(window_5, text="Enter value of Apparent Facial Tension "
                                                               "(dyn/cm):", font=("Satoshi", 10, "bold"))
            app_facial_tension_label.grid(row=2, column=0)

            def back5():
                window_5.withdraw()
                select.deiconify()

            def compute_rft():
                k = float(c_factor.get())
                m = float(app_facial_tension.get())
                rft = k * m

                real_facial_tension_label = tk.Label(window_5, text=f"The Facial Tension (De Nouy Ring Method)"
                                                                    f"is: {round(rft, 2)} "
                                                                    f"dyn/cm.", font=("Satoshi", 10, "bold"))
                real_facial_tension_label.grid(row=3, column=0)

            c_factor = tk.Entry(window_5)
            c_factor.grid(row=1, column=1)

            app_facial_tension = tk.Entry(window_5)
            app_facial_tension.grid(row=2, column=1)

            compute = tk.Button(window_5, text="Compute", font="Satoshi", command=compute_rft)
            compute.grid(row=4, column=1)

            back_button5 = tk.Button(window_5, text="Back", font="Satoshi", command=back5)
            back_button5.grid(row=4, column=0)

            window_5.mainloop()

        def window6():
            select.withdraw()
            window_6 = tk.Tk()
            window_6.title("PetroCalc")

            title7_label = tk.Label(window_6, text="Liquid Permeability (permeameter lab "
                                                   "measurement)", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title7_label.grid(row=0, column=0)

            v_liquid_label = tk.Label(window_6, text="Enter value of the Viscosity of Liquid Phase "
                                                     "(cP):", font=("Satoshi", 10, "bold"))
            v_liquid_label.grid(row=1, column=0)

            time_label = tk.Label(window_6, text="Enter value of Flowing Time "
                                                 "(s):", font=("Satoshi", 10, "bold"))
            time_label.grid(row=2, column=0)

            liquid_volume_label = tk.Label(window_6, text="Enter value of Liquid Volume that flows in time-Burette "
                                                          "Volume "
                                                          "(cm³):", font=("Satoshi", 10, "bold"))
            liquid_volume_label.grid(row=3, column=0)

            pressure_label = tk.Label(window_6, text="Enter value of Pressure value that read from Pressure "
                                                     "Gauge (Atm):", font=("Satoshi", 10, "bold"))
            pressure_label.grid(row=4, column=0)

            length_label = tk.Label(window_6, text="Enter value of Plug Length (cm):", font=("Satoshi", 10, "bold"))
            length_label.grid(row=5, column=0)

            open_flow_area_label = tk.Label(window_6, text="Enter value of Open-Flow Area of the Plug "
                                                           "(cm²):", font=("Satoshi", 10, "bold"))
            open_flow_area_label.grid(row=6, column=0)

            def back6():
                window_6.withdraw()
                select.deiconify()

            def compute_lp():
                n = float(v_liquid.get())
                o = float(time.get())
                p = float(liquid_volume.get())
                q = float(pressure.get())
                r = float(length.get())
                s = float(open_flow_area.get())
                permeability = (n * p * r) / (s * q * o)

                l_permeability_label = tk.Label(window_6, text=f"The computed Liquid Permeability (permeameter lab "
                                                               f"measurement) is: {round(permeability, 2)} "
                                                               f"D.", font=("Satoshi", 10, "bold"))
                l_permeability_label.grid(row=7, column=0)

            v_liquid = tk.Entry(window_6)
            v_liquid.grid(row=1, column=1)

            time = tk.Entry(window_6)
            time.grid(row=2, column=1)

            liquid_volume = tk.Entry(window_6)
            liquid_volume.grid(row=3, column=1)

            pressure = tk.Entry(window_6)
            pressure.grid(row=4, column=1)

            length = tk.Entry(window_6)
            length.grid(row=5, column=1)

            open_flow_area = tk.Entry(window_6)
            open_flow_area.grid(row=6, column=1)

            compute = tk.Button(window_6, text="Compute", font="Satoshi", command=compute_lp)
            compute.grid(row=8, column=1)

            back_button6 = tk.Button(window_6, text="Back", font="Satoshi", command=back6)
            back_button6.grid(row=8, column=0)

            window_6.mainloop()

        def window7():
            select.withdraw()
            window_7 = tk.Tk()
            window_7.title("PetroCalc")

            title8_label = tk.Label(window_7, text="Relative Centrifugal "
                                                   "Force", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title8_label.grid(row=0, column=0)

            rpm_label = tk.Label(window_7, text="Enter value of Revolutions per Minute "
                                                "(rpm):", font=("Satoshi", 10, "bold"))
            rpm_label.grid(row=1, column=0)

            diameter_label = tk.Label(window_7, text="Enter value of Expansion Diameter between two confronted "
                                                     "tubes (inches (in.)):", font=("Satoshi", 10, "bold"))
            diameter_label.grid(row=2, column=0)

            def back7():
                window_7.withdraw()
                select.deiconify()

            def compute_rcf():
                t = float(rpm.get())
                u = float(diameter.get())
                rcf = (t / 265) ** 2 * u
                relative_centrifugal_label = tk.Label(window_7, text=f"The computed Relative Centrifugal Force "
                                                                     f"is: {round(rcf, 2)} "
                                                                     f"cP.", font=("Satoshi", 10, "bold"))
                relative_centrifugal_label.grid(row=3, column=0)

            rpm = tk.Entry(window_7)
            rpm.grid(row=1, column=1)

            diameter = tk.Entry(window_7)
            diameter.grid(row=2, column=1)

            compute = tk.Button(window_7, text="Compute", font="Satoshi", command=compute_rcf)
            compute.grid(row=4, column=1)

            back_button7 = tk.Button(window_7, text="Back", font="Satoshi", command=back7)
            back_button7.grid(row=4, column=0)

            window_7.mainloop()

        def window8():
            select.withdraw()
            window_8 = tk.Tk()
            window_8.title("PetroCalc")

            title9_label = tk.Label(window_8, text="Resistance", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title9_label.grid(row=0, column=0)

            potential_drop_label = tk.Label(window_8, text="Enter value of Potential Drop "
                                                           "(V):", font=("Satoshi", 10, "bold"))
            potential_drop_label.grid(row=1, column=0)

            current_label = tk.Label(window_8, text="Enter value of Current "
                                                    "(A):", font=("Satoshi", 10, "bold"))
            current_label.grid(row=2, column=0)

            def back8():
                window_8.withdraw()
                select.deiconify()

            def compute_resistance():
                v = float(potential_drop.get())
                w = float(current.get())
                resistance = v / w
                resistance_label = tk.Label(window_8, text=f"The computed Resistance is: {round(resistance, 2)} "
                                                           f"ohm.", font=("Satoshi", 10, "bold"))
                resistance_label.grid(row=3, column=0)

            potential_drop = tk.Entry(window_8)
            potential_drop.grid(row=1, column=1)

            current = tk.Entry(window_8)
            current.grid(row=2, column=1)

            compute = tk.Button(window_8, text="Compute", font="Satoshi", command=compute_resistance)
            compute.grid(row=4, column=1)

            back_button8 = tk.Button(window_8, text="Back", font="Satoshi", command=back8)
            back_button8.grid(row=4, column=0)

            window_8.mainloop()

        def window9():
            select.withdraw()
            window_9 = tk.Tk()
            window_9.title("PetroCalc")

            title10_label = tk.Label(window_9, text="Resistivity", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title10_label.grid(row=0, column=0)

            resistance2_label = tk.Label(window_9, text="Enter value of Resistance "
                                                        "(in ohm):", font=("Satoshi", 10, "bold"))
            resistance2_label.grid(row=1, column=0)

            cs_area_label = tk.Label(window_9, text="Enter value of Cross Section Area "
                                                    "(m²):", font=("Satoshi", 10, "bold"))
            cs_area_label.grid(row=2, column=0)

            length2_label = tk.Label(window_9, text="Enter value of Length (m):", font=("Satoshi", 10, "bold"))
            length2_label.grid(row=3, column=0)

            def back9():
                window_9.withdraw()
                select.deiconify()

            def compute_resistivity():
                x = float(resistance2.get())
                y = float(cs_area.get())
                z = float(length2.get())
                resistivity = x * y / z
                resistance_label = tk.Label(window_9, text=f"The computed Resistivity "
                                                           f"is: {round(resistivity, 2)} "
                                                           f"ohm*m.", font=("Satoshi", 10, "bold"))
                resistance_label.grid(row=4, column=0)

            resistance2 = tk.Entry(window_9)
            resistance2.grid(row=1, column=1)

            cs_area = tk.Entry(window_9)
            cs_area.grid(row=2, column=1)

            length2 = tk.Entry(window_9)
            length2.grid(row=3, column=1)

            compute = tk.Button(window_9, text="Compute", font="Satoshi", command=compute_resistivity)
            compute.grid(row=5, column=1)

            back_button9 = tk.Button(window_9, text="Back", font="Satoshi", command=back9)
            back_button9.grid(row=5, column=0)

            window_9.mainloop()

        def window10():
            select.withdraw()
            window_10 = tk.Tk()
            window_10.title("PetroCalc")

            title11_label = tk.Label(window_10, text="Resistivity Index - Archie's "
                                                     "Law", font=("Satoshi", 12, "bold"), fg="#1c407d")
            title11_label.grid(row=0, column=0)

            true_resistivity_label = tk.Label(window_10, text="Enter value of True Resistivity "
                                                              "(ohm*m):", font=("Satoshi", 10, "bold"))
            true_resistivity_label.grid(row=1, column=0)

            rock_resistivity_label = tk.Label(window_10, text="Enter value of Resistivity of Rock Filled "
                                                              "with Water "
                                                              "(ohm*m):", font=("Satoshi", 10, "bold"))
            rock_resistivity_label.grid(row=2, column=0)

            def back10():
                window_10.withdraw()
                select.deiconify()

            def compute_tresistance():
                aa = float(true_resistivity.get())
                ab = float(rock_resistivity.get())
                resistivity_index = aa / ab
                resistivity_index_label = tk.Label(window_10, text=f"The computed Resistivity Index - Archie's "
                                                                   f"Law is: {round(resistivity_index, 2)} "
                                                                   f"(unitless).", font=("Satoshi", 10, "bold"))
                resistivity_index_label.grid(row=3, column=0)

            true_resistivity = tk.Entry(window_10)
            true_resistivity.grid(row=1, column=1)

            rock_resistivity = tk.Entry(window_10)
            rock_resistivity.grid(row=2, column=1)

            compute = tk.Button(window_10, text="Compute", font="Satoshi", command=compute_tresistance)
            compute.grid(row=4, column=1)

            back_button10 = tk.Button(window_10, text="Back", font="Satoshi", command=back10)
            back_button10.grid(row=4, column=0)

            window_10.mainloop()

        root.withdraw()
        select = tk.Tk()
        select.title("PetroCalc")

        select_label0 = tk.Label(select, text="Petroleum Laboratory "
                                              "Lessons", font=("Satoshi", 14, "bold"), fg="#1c407d")

        select_label0.grid(row=0, column=0)

        select_label1 = tk.Label(select, text="1. Adhesion Tension\n" "2. Amott-Harvey Wetability Index\n"
                                              "3. Apparent Facial Tension (De Nouy Ring Method)\n"
                                              "4. Average Gas Solubility\n" "5. Facial Tension (De Nouy Ring Method)\n"
                                              "6. Liquid Permeability (permeameter lab measurement)\n" "7. Relative "
                                              "Centrifugal Force\n" "8. Resistance\n" "9. Resistivity\n" 
                                              "10. Resistivity Index - "
                                              "Archie's Law", font=("Satoshi", 11,
                                                                    "bold"), justify=tk.LEFT)
        select_label1.grid(row=1, column=0)

        select_label2 = tk.Label(select, text="Please select a Petroleum Engineering Laboratory Lesson to Calculate ("
                                              "1-10):", font=("Satoshi", 9, "bold"))
        select_label2.grid(row=2, column=0)

        enter = tk.Entry(select)
        enter.grid(row=3, column=0)

        def path1():
            number = enter.get()
            if number == "1":
                window1()
            elif number == "2":
                window2()
            elif number == "3":
                window3()
            elif number == "4":
                window4()
            elif number == "5":
                window5()
            elif number == "6":
                window6()
            elif number == "7":
                window7()
            elif number == "8":
                window8()
            elif number == "9":
                window9()
            elif number == "10":
                window10()
            else:
                messagebox.showerror("Error", "Only select a number from 1-10.")

        go_button = tk.Button(select, text="Enter", width=8, font="Satoshi", command=path1)
        go_button.grid(row=4, column=0)

        back_button = tk.Button(select, text="Back", font="Satoshi", command=back)
        back_button.grid(row=5, column=0)

        select.mainloop()

    title_label = tk.Label(root, text="Welcome to PetroCalc:\n Mastering Laboratory Formulas in Petroleum "
                                      "Engineering!", font=("Satoshi", 15, "bold"), fg="#1c407d")
    title_label.grid(row=0, column=0)
    button = tk.Button(root, text="Continue", width=10, font="Satoshi", command=choose)
    button.grid(row=1, column=0)

    root.mainloop()


menu()
