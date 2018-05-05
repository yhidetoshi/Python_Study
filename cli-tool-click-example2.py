import click

@click.command(help='Simple click CLI')
@click.option('-n', '--name', 'name', type=str, help='your name', required=True)
@click.option('-l', '--last-name', 'last_name', type=str, help='your last name', default='YAMADA', required=False)

def main(name, last_name):
    print("Your name is %s" % name)

if __name__ == '__main__':
    main()

"""
~/P/CLI-Tool ❯❯❯ python test1.py -n yajima
Your name is yajima
~/P/CLI-Tool ❯❯❯ python test1.py --name yajima
Your name is yajima
"""
