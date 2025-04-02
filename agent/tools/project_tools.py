# Project file processing tool for AI Agent

import os
import json
from datetime import datetime, timedelta


class ProjectFileProcessor:
    """
    Tool for processing and analyzing project management files.
    This is a simulated implementation of MPXJ integration.
    """
    
    @staticmethod
    def extract_tasks(file_path):
        """
        Extract tasks from a project file.
        
        Args:
            file_path (str): The path to the project file.
        
        Returns:
            str: The extracted tasks.
        """
        # In a real implementation, this would use MPXJ to extract tasks
        # For demonstration, we'll return simulated results
        
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."
        
        file_extension = os.path.splitext(file_path)[1].lower()
        
        # Simulate different file format support
        supported_formats = [".mpp", ".mpx", ".xml", ".xer", ".p6xml"]
        
        if file_extension not in supported_formats:
            return f"Error: Unsupported file format {file_extension}. Supported formats are: {', '.join(supported_formats)}"
        
        # Simulate task extraction
        today = datetime.now()
        
        tasks = [
            {
                "id": 1,
                "name": "Project Initiation",
                "start_date": (today + timedelta(days=1)).strftime("%Y-%m-%d"),
                "end_date": (today + timedelta(days=5)).strftime("%Y-%m-%d"),
                "duration": "5d",
                "resources": ["Project Manager", "Business Analyst"],
                "predecessors": []
            },
            {
                "id": 2,
                "name": "Requirements Analysis",
                "start_date": (today + timedelta(days=6)).strftime("%Y-%m-%d"),
                "end_date": (today + timedelta(days=15)).strftime("%Y-%m-%d"),
                "duration": "10d",
                "resources": ["Business Analyst", "Domain Expert"],
                "predecessors": [1]
            },
            {
                "id": 3,
                "name": "System Design",
                "start_date": (today + timedelta(days=16)).strftime("%Y-%m-%d"),
                "end_date": (today + timedelta(days=30)).strftime("%Y-%m-%d"),
                "duration": "15d",
                "resources": ["Solution Architect", "UI Designer"],
                "predecessors": [2]
            }
        ]
        
        # Format the results as a string
        formatted_results = f"Tasks extracted from {file_path}:\n"
        for task in tasks:
            formatted_results += f"\nTask ID: {task['id']}\n"
            formatted_results += f"Name: {task['name']}\n"
            formatted_results += f"Duration: {task['duration']}\n"
            formatted_results += f"Start: {task['start_date']} | End: {task['end_date']}\n"
            formatted_results += f"Resources: {', '.join(task['resources'])}\n"
            formatted_results += f"Predecessors: {', '.join(map(str, task['predecessors']))}\n"
        
        return formatted_results
    
    @staticmethod
    def extract_resources(file_path):
        """
        Extract resources from a project file.
        
        Args:
            file_path (str): The path to the project file.
        
        Returns:
            str: The extracted resources.
        """
        # In a real implementation, this would use MPXJ to extract resources
        # For demonstration, we'll return simulated results
        
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."
        
        file_extension = os.path.splitext(file_path)[1].lower()
        
        # Simulate different file format support
        supported_formats = [".mpp", ".mpx", ".xml", ".xer", ".p6xml"]
        
        if file_extension not in supported_formats:
            return f"Error: Unsupported file format {file_extension}. Supported formats are: {', '.join(supported_formats)}"
        
        # Simulate resource extraction
        resources = [
            {
                "id": 1,
                "name": "Project Manager",
                "role": "Management",
                "cost": "$100/h"
            },
            {
                "id": 2,
                "name": "Business Analyst",
                "role": "Analysis",
                "cost": "$80/h"
            },
            {
                "id": 3,
                "name": "Solution Architect",
                "role": "Design",
                "cost": "$120/h"
            },
            {
                "id": 4,
                "name": "UI Designer",
                "role": "Design",
                "cost": "$90/h"
            },
            {
                "id": 5,
                "name": "Domain Expert",
                "role": "Analysis",
                "cost": "$95/h"
            }
        ]
        
        # Format the results as a string
        formatted_results = f"Resources extracted from {file_path}:\n"
        for resource in resources:
            formatted_results += f"\nResource ID: {resource['id']}\n"
            formatted_results += f"Name: {resource['name']}\n"
            formatted_results += f"Role: {resource['role']}\n"
            formatted_results += f"Cost: {resource['cost']}\n"
        
        return formatted_results
    
    @staticmethod
    def analyze_project(file_path):
        """
        Analyze a project file and provide insights.
        
        Args:
            file_path (str): The path to the project file.
        
        Returns:
            str: The project analysis.
        """
        # In a real implementation, this would use MPXJ to analyze the project
        # For demonstration, we'll return simulated results
        
        if not os.path.exists(file_path):
            return f"Error: File {file_path} not found."
        
        file_extension = os.path.splitext(file_path)[1].lower()
        
        # Simulate different file format support
        supported_formats = [".mpp", ".mpx", ".xml", ".xer", ".p6xml"]
        
        if file_extension not in supported_formats:
            return f"Error: Unsupported file format {file_extension}. Supported formats are: {', '.join(supported_formats)}"
        
        # Simulate project analysis
        today = datetime.now()
        
        project_info = {
            "name": "Sample Project",
            "start_date": (today + timedelta(days=1)).strftime("%Y-%m-%d"),
            "end_date": (today + timedelta(days=60)).strftime("%Y-%m-%d"),
            "duration": "60d",
            "task_count": 32,
            "resource_count": 12,
            "critical_path_length": "45d",
            "total_cost": "$125,000",
            "risks": [
                "Resource allocation conflicts in week 3",
                "Task dependencies may create bottlenecks",
                "Timeline constraints with external vendors"
            ],
            "recommendations": [
                "Consider adding buffer time to critical path tasks",
                "Review resource allocation for optimization",
                "Identify tasks that can be parallelized"
            ]
        }
        
        # Format the results as a string
        formatted_results = f"Project Analysis for {file_path}:\n\n"
        formatted_results += f"Project Name: {project_info['name']}\n"
        formatted_results += f"Duration: {project_info['duration']} ({project_info['start_date']} to {project_info['end_date']})\n"
        formatted_results += f"Task Count: {project_info['task_count']}\n"
        formatted_results += f"Resource Count: {project_info['resource_count']}\n"
        formatted_results += f"Critical Path: {project_info['critical_path_length']}\n"
        formatted_results += f"Total Estimated Cost: {project_info['total_cost']}\n\n"
        
        formatted_results += "Identified Risks:\n"
        for i, risk in enumerate(project_info['risks'], 1):
            formatted_results += f"{i}. {risk}\n"
        
        formatted_results += "\nRecommendations:\n"
        for i, recommendation in enumerate(project_info['recommendations'], 1):
            formatted_results += f"{i}. {recommendation}\n"
        
        return formatted_results
    
    @staticmethod
    def convert_project_file(source_path, target_format):
        """
        Convert a project file to a different format.
        
        Args:
            source_path (str): The path to the source project file.
            target_format (str): The target format (e.g., 'mpp', 'xml', 'xer').
        
        Returns:
            str: The result of the conversion.
        """
        # In a real implementation, this would use MPXJ to convert the file
        # For demonstration, we'll return simulated results
        
        if not os.path.exists(source_path):
            return f"Error: File {source_path} not found."
        
        file_extension = os.path.splitext(source_path)[1].lower()
        
        # Simulate different file format support
        supported_formats = [".mpp", ".mpx", ".xml", ".xer", ".p6xml"]
        
        if file_extension not in supported_formats:
            return f"Error: Unsupported source format {file_extension}. Supported formats are: {', '.join(supported_formats)}"
        
        # Check target format
        target_format = target_format.lower()
        supported_target_formats = ["mpp", "mpx", "xml", "xer", "p6xml"]
        
        if target_format not in supported_target_formats:
            return f"Error: Unsupported target format {target_format}. Supported formats are: {', '.join(supported_target_formats)}"
        
        # Generate target path
        source_dir = os.path.dirname(source_path)
        source_name = os.path.splitext(os.path.basename(source_path))[0]
        target_path = os.path.join(source_dir, f"{source_name}.{target_format}")
        
        # Simulate conversion
        return f"Project file conversion:\n\nSource: {source_path}\nTarget: {target_path}\n\nConversion completed successfully. The project has been converted to {target_format.upper()} format."
