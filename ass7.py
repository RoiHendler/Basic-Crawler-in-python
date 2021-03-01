def get_file_content():
    pass


def crawl(file_path, all_links):
    file = open(file_path, "r")
    file_content = file.read()
    links_from_file = parser(file_content)

    all_links[file_path] = links_from_file

    for i in range(0, len(links_from_file)):
        current_link = links_from_file[i]
        if current_link not in all_links:
            crawl(current_link, all_links)


def parser(html_content):
    links_from_html = list()
    link_identifier = 'href="'
    index = html_content.find(link_identifier)
    while index != -1:
        start_link_index = index + 6
        end_link_index = html_content.find('"', start_link_index)
        link = html_content[start_link_index:end_link_index]
        links_from_html.append(link)
        index = html_content.find(link_identifier, end_link_index + 1)
    return links_from_html


def save_to_file(all_links, dest_file):
    keys_sorted = list(all_links.keys())
    keys_sorted.sort()

    str = ''
    for key in keys_sorted:
        str += '{file},{links}'.format(file=key, links=','.join(all_links[key]))
        str += '\n'

    file = open(dest_file, "w")
    file.write(str)
    file.close()


def print_file_links(all_links):
    file_name = input('\nenter file name:\n')
    file_links = all_links[file_name]
    file_links.sort()
    print(file_links)


def main():
    all_links = dict()
    start_file = input('enter source file:')
    crawl(start_file, all_links)
    save_to_file(all_links, 'results.csv')
    print_file_links(all_links)


if __name__ == '__main__':
    main()
