# CLI-Project-Management-System
# **Project Management System Script**  
This script provides a lightweight solution for managing projects, categorizing them as active or inactive, and tracking their progress. The code is designed to simplify project tracking while ensuring extensibility for future enhancements.  
---
## **Features**
- **Project Management:** Add, update, delete, and view project details.  
- **Project Status Tracking:** Distinguish between active and inactive projects.  
- **Extensibility:** Modular design allows for the easy addition of new features.  
- **Data Storage:** Project data is stored in-memory for simplicity but can be extended to use a database or external storage.  
---
## **Modules**
### **1. Project Management Functions**
- **`add_project(project_id, name, status)`**  
 Adds a new project with a unique ID, name, and status (active/inactive).  
- **`update_project(project_id, name=None, status=None)`**  
 Updates the details of an existing project, such as its name or status.  
- **`delete_project(project_id)`**  
 Removes a project based on its ID.  
- **`list_projects(status=None)`**  
 Lists all projects. If `status` is specified, only projects with that status (active/inactive) are listed.  
---
## **Installation**  
1. **Prerequisites:**  
  - Python 3.7 or higher  
2. **Clone the Repository:**  
  ```bash  
  git clone <repository_url>  
  cd project-management-system  
  ```  
3. **Install Dependencies:**  
  *(No external dependencies are required for this script)*  
4. **Run the Script:**  
  ```bash  
  python script_name.py  
  ```  
---
## **Usage**  
### Example Workflow  
1. **Add Projects:**  
  ```python  
  add_project(1, "Project Alpha", "active")  
  add_project(2, "Project Beta", "inactive")  
  ```  
2. **Update Project:**  
  ```python  
  update_project(1, name="Updated Project Alpha", status="inactive")  
  ```  
3. **Delete Project:**  
  ```python  
  delete_project(2)  
  ```  
4. **List All Projects:**  
  ```python  
  list_projects()  
  ```  
5. **List Active Projects:**  
  ```python  
  list_projects("active")  
  ```  
---
## **File Structure**  
```
project-management-system/
├── script_name.py   # Main project management script
└── README.md        # Documentation  
```  
---
## **Future Enhancements**
1. Integrate database storage (e.g., SQLite, MySQL).  
2. Add a web interface for project management.  
3. Implement user authentication for multi-user access.  
4. Support advanced filtering and reporting capabilities.  
---
## **Contact**  
For any queries or contributions, feel free to contact:  
Pratik Tushar Gade
Contact: 9923418841
