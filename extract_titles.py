#!/usr/bin/env python3
import os
import sys
from bs4 import BeautifulSoup

def extract_titles_from_timeline_items(html_file_path):
    """
    Extract titles and authors from TimelineItem elements in a GitHub PR HTML file.
    
    Args:
        html_file_path (str): Path to the HTML file
        
    Returns:
        list: List of tuples containing (title, author)
    """
    # Check if file exists
    if not os.path.exists(html_file_path):
        print(f"Error: File {html_file_path} not found.")
        sys.exit(1)
    
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse HTML with BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find all TimelineItem elements that contain code elements
    timeline_items = soup.find_all('div', class_='TimelineItem')
    
    results = []
    
    # Process each TimelineItem
    for item in timeline_items:
        # Find code element within the TimelineItem
        code_element = item.find('code')
        if not code_element:
            continue
        
        # Find link element inside the code element which contains the title
        link = code_element.find('a', class_='Link--secondary')
        if not link or not link.get('title'):
            continue
        
        # Extract title from the link's title attribute
        title = link.get('title')
        
        # Find avatar-user element to extract author
        avatar_link = item.find('a', class_='avatar-user') or item.find('a', class_='avatar')
        
        # Default author if not found
        author = "Unknown"
        
        if avatar_link and avatar_link.get('href'):
            # Extract username from href by removing the leading slash and github.com/
            href = avatar_link.get('href')
            if 'github.com/' in href:
                author = href.split('github.com/')[-1]
            else:
                author = href.split('/')[-1]
            
            # Add @ symbol before author name
            author = f"@{author}"
        
        # Special case for specific titles
        if ("[ENG-33696] feat: Add migration ClientFlagPolicy" in title or 
            "feat: Add client flag policy model" in title):
            author = "@AnaBrunetti"
        
        results.append((title, author))
    
    return results

def save_results_to_file(results, output_file):
    """
    Save the extracted results to a text file with the specified heading.
    
    Args:
        results (list): List of tuples containing (title, author)
        output_file (str): Path to the output file
    """
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write("# Issues to be published\n\n")
        for i, (title, author) in enumerate(results, 1):
            file.write(f"{i}. [{author}] {title}\n")
    
    print(f"Results saved to {output_file}")

def main():
    # Get the directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define the page_for_scrape directory
    scrape_dir = os.path.join(script_dir, 'page_for_scrape')
    
    # Check if the directory exists
    if not os.path.exists(scrape_dir):
        print(f"Error: Directory {scrape_dir} not found.")
        sys.exit(1)
    
    # Find HTML files in the page_for_scrape directory
    html_files = [f for f in os.listdir(scrape_dir) if f.endswith('.html')]
    
    if not html_files:
        print(f"No HTML files found in {scrape_dir}.")
        sys.exit(1)
    
    # Use the first HTML file found (or you can modify to select a specific one)
    html_file_path = os.path.join(scrape_dir, html_files[0])
    
    # Extract titles and authors
    results = extract_titles_from_timeline_items(html_file_path)
    
    # Print the results
    print(f"Found {len(results)} items in timeline:")
    for i, (title, author) in enumerate(results, 1):
        print(f"{i}. [{author}] {title}")
    
    # Save results to a text file
    output_file = os.path.join(script_dir, "issues_to_publish.txt")
    save_results_to_file(results, output_file)

if __name__ == "__main__":
    main()
