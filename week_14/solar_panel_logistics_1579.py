def create_model(n_panels, trucks, shipping_cost, panels):
    pass


def solar_panel_logistics():

    days = int(input())

    while days > 0:

        n_panels, trucks, shipping = list(map(int, input().split()))

        panels = list(map(int, input().split()))

        create_model(n_panels, trucks, shipping, panels)

        days -= 1


if __name__ == '__main__':
    solar_panel_logistics()
