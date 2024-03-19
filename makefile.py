.PHONY: run install clean 

run: 
    python main.py 
    
install: 
    pip install -r requirements.txt 
    
clean: 
    find . -name "*.pyc" -exec rm -f {} + 
    find . -name "__pycache__" -exec rm -rf {} +  
    rm -rf build/ dist/ *.egg-info/ 
    
