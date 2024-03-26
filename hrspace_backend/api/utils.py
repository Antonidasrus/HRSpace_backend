def istartswith_search(queryset, self):
    """
    Поиск по частичному вхождению
    в начале названия.
    """
    name = self.request.query_params.get("name")
    if name:
        queryset = queryset.filter(name__istartswith=name)
    return queryset
