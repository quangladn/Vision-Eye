import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Vision Eye Engine', width=600, height=500)

with dpg.window(label="Example Window", width=200,height=200, no_close=True):
    dpg.add_text("Hello, world")
    dpg.add_button(label="Save",callback=lambda: print(123))
    dpg.add_input_text(label="string", default_value="Quick brown fox",callback=
                         lambda _, __: print(__))
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1,callback=
                         lambda _, __: print(__))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()