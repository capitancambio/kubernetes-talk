# `my_slide_config.py` 
# This allows hiding input cells that have a "to_remove" tag
# See https://github.com/jupyterlab/jupyterlab/issues/4100#issuecomment-370938358
c.TagRemovePreprocessor.remove_input_tags = {"hide_input"}
c.TagRemovePreprocessor.remove_all_outputs_tags = {"hide_output"}
c.TagRemovePreprocessor.remove_cell_tags= {"hide"}
c.SlidesExporter.reveal_theme="simple"

# the following does the equivalent of --to slides and --post serve, see here: https://github.com/jupyter/nbconvert/blob/master/setup.py#L220 + https://github.com/jupyter/nbconvert/blob/master/nbconvert/nbconvertapp.py#L482 and here https://github.com/jupyter/nbconvert/blob/master/nbconvert/nbconvertapp.py#L238
app_settings = {
#     "postprocessor_class": "nbconvert.postprocessors.serve.ServePostProcessor",
    "export_format": "slides"
}
c.NbConvertApp.update(app_settings)

# the following does the equivalent of --no-prompt, see here: https://github.com/jupyter/nbconvert/blob/master/nbconvert/nbconvertapp.py#L109-L114
exporter_settings = {
    'exclude_input_prompt' : True,
    'exclude_output_prompt' : True,
}
c.TemplateExporter.update(exporter_settings)
