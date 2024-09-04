Copart Lot Price Analysis Tool
Overview
The Copart Lot Price Analysis Tool is a web-based application designed to assist individuals who buy vehicles on Copart, repair them, and sell them for profit. By automating the process of gathering and analyzing vehicle prices, this tool saves time and provides valuable insights into the potential profitability of a purchase.
Features:
    Input Field for Copart Lot Number: Users can enter a Copart lot number into the input field to begin the analysis.

    Data Gathering: The tool scrapes data from Copart to retrieve detailed information about the vehicle.

    Price Comparison: The tool searches for cars with the same specifications on the Georgian car-selling platform Myauto.

    Price Calculation: It calculates the minimum, maximum, and mean prices of the specific car, helping users to assess the market value.

    Automated Analysis: Ideal for buyers who repair and resell vehicles, automating the necessary work to determine a vehicle's resale value.
How It Works:
    Copart Lot Search: The user enters the Copart lot number, and the tool retrieves detailed information about the vehicle from Copart.
    Users can also choose which details they want to ignore during search.
    ![image](https://github.com/user-attachments/assets/15acd450-e7f9-41b9-9de8-0eb2c7f96b87)


    Myauto Search: The tool searches Myauto for cars with the same specifications as the one from Copart.

    Price Analysis: The tool gathers the prices from Myauto and calculates the minimum, maximum, and mean prices.

    Result Display: The analysis is displayed on a single page, providing a clear and concise overview of the car's potential market value.
    ![image](https://github.com/user-attachments/assets/806a8d12-7b37-4a74-8dc3-0118fa80ec52)

Technologies Used:
    Python: For backend logic and data processing.
    Flask: To create the web interface and manage user requests.
    Selenium: For web scraping, especially interacting with dynamic content on Copart and Myauto.
    HTML/CSS: For the frontend design.
Installation
    Clone the repository:
      git clone https://github.com/yourusername/copart-lot-price-analysis-tool.git

    Navigate to the project directory:
      cd copart-lot-price-analysis-tool

    Install the required dependencies:
      pip install -r requirements.txt

    Run the application:
      python app.py

    open your browser and navigate to http://localhost:5000 to use the tool.
    
  Future Improvements:

    Optimal Purchase Price Calculation: Implement functionality to calculate the optimal price to buy the car based on repair costs and potential resale value.

    Shipping Cost Integration: Gather data from import companies to calculate shipping costs and factor this into the overall cost analysis.
