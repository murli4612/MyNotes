import sys
import os
import time

# Ensure project root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flipkart.models.enums import ProjectCategory
from flipkart.services.thrive import ThrivePlatform

def run_test_scenario():
    print("=== Running Talent Pool Platform Test Scenario ===")
    platform = ThrivePlatform()

    # 1. Register leads
    print("\n1. Registering leads:")
    print(platform.register_lead("Lead1"))
    print(platform.register_lead("Lead2"))

    # 2. Register developers
    print("\n2. Registering developers:")
    print(platform.register_developer("Dev1"))
    print(platform.register_developer("Dev2"))

    # 3. Register long-term projects
    print("\n3. Registering projects:")
    print(platform.register_project("Lead2", "App Development", ProjectCategory.FRONTEND))
    print(platform.register_project("Lead1", "K8s cluster setup", ProjectCategory.DEVOPS))

    # 4. Get available projects
    print("\n4. Available projects:")
    projects = platform.get_available_projects()
    if not projects:
        print("No available projects found. Exiting test.")
        return

    for p in projects:
        print(f"{p['id']}, {p['name']}, {p['category']}, {p['lead']}")

    # 5. Request project
    print("\n5. Requesting project:")
    try:
        project_id = projects[0]['id']
        print(platform.request_project("Dev1", project_id))
    except IndexError:
        print("No projects available to request.")
        return

    # 6. Accept request
    print("\n6. Accepting request:")
    try:
        request_id = next(iter(platform.requests.keys()))
        print(platform.accept_request("Lead2", request_id))
    except StopIteration:
        print("No requests found to accept.")
        return

    # 7. Developer details
    print("\n7. Developer details:")
    print(platform.get_developer_details("Dev1"))
    print(platform.get_developer_details("Dev2"))

    # 8. Project details
    print("\n8. Project details:")
    try:
        print(platform.get_project_details(project_id))
        other_project_id = projects[1]['id']
        print(platform.get_project_details(other_project_id))
    except IndexError:
        print("Second project not found for detail display.")
        other_project_id = None

    # 9. Completing project
    print("\n9. Completing project:")
    try:
        print(platform.start_project("Dev1", project_id))
        print(platform.complete_project("Dev1", project_id, 4))
    except Exception as e:
        print(f"Error while completing project: {e}")

    # 10. Cancel another project
    if other_project_id:
        print("\n10. Canceling another project:")
        try:
            print(platform.cancel_project("Lead1", other_project_id))
        except Exception as e:
            print(f"Error while canceling project: {e}")
    else:
        print("\n10. No second project to cancel.")

    # 11. Project expiry demonstration
    print("\n11. Project expiry demonstration:")
    print("- Registering temporary project (expires in 1 minute):")
    try:
        print(platform.register_project("Lead1", "Temporary Project", ProjectCategory.DEVOPS, expiry_minutes=1))
    except TypeError:
        print("register_project() does not support 'expiry_minutes'. Please update your ThrivePlatform method.")

    # Get temp project ID
    temp_projects = platform.get_available_projects()
    temp_project_id = next((p['id'] for p in temp_projects if p['name'] == "Temporary Project"), None)
    if temp_project_id:
        print(f"- Temporary project ID: {temp_project_id}")
        print("- Waiting for 1 minute for the project to expire...")
        time.sleep(60)

        print("- Checking temporary project status after expiry:")
        try:
            project = platform.get_project_details(temp_project_id)
            print(project)
        except Exception as e:
            print(f"Error: {str(e)} (project has been automatically cancelled due to expiry)")
    else:
        print("Error: Temporary project not found.")

    print("\n=== Test Scenario Completed ===")

if __name__ == "__main__":
    run_test_scenario()
