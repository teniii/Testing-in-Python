def pre_mutation(context):
    line = context.current_source_line.strip()
    if line.startswith('raise') or line.startswith('"'):
        context.skip = True
