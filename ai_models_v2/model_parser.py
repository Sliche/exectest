import json
import os


class ModelParser():

    def extract_prediction_endpoint_parameters(self, openapi_schema):
        """
        Extracts the parameters required for the 'prediction' endpoint from the OpenAPI schema.

        Args:
        - openapi_schema (dict): The OpenAPI schema part of the model information.

        Returns:
        - dict: A dictionary with parameter names as keys and their specifications as values.
        """
        # Initialize an empty dictionary to hold the parameter specifications
        parameters_spec = {}

        # Access the 'Input' schema which contains the prediction parameters
        input_schema = openapi_schema.get("components", {}).get("schemas", {}).get("Input", {}).get("properties", {})

        # Iterate over the input schema properties to extract required details
        for param, details in input_schema.items():
            # Extracting the basic information
            param_spec = {
                "type": details.get("type"),
                "description": details.get("description", "No description available."),
                "default": details.get("default"),
                "constraints": {}
            }

            # Translate model types to those used by streamzero
            param_spec["type"] = "float" if param_spec["type"] == "number" else param_spec["type"]
            param_spec["type"] = "int" if param_spec["type"] == "integer" else param_spec["type"]
            param_spec["type"] = "text" if param_spec["type"] == "string" else param_spec["type"]

            # Extracting constraints if available (e.g., minimum, maximum for numbers)
            if "minimum" in details:
                param_spec["constraints"]["minimum"] = details["minimum"]
            if "maximum" in details:
                param_spec["constraints"]["maximum"] = details["maximum"]
            if "minLength" in details:
                param_spec["constraints"]["minLength"] = details["minLength"]
            if "maxLength" in details:
                param_spec["constraints"]["maxLength"] = details["maxLength"]
            if "enum" in details:
                param_spec["constraints"]["enum"] = details["enum"]
            if "format" in details:
                param_spec["constraints"]["format"] = details["format"]

            # Add the parameter specification to the dictionary
            parameters_spec[param] = param_spec

        return parameters_spec

    def create_readme(self, openapi_schema):
        parameters_spec = self.extract_prediction_endpoint_parameters(openapi_schema)

        # Iterate through each top-level attribute in the parameters dictionary
        for attribute, details in parameters_spec.items():
            # print(f"Attribute: {attribute}")
            # print(f"Type: {details['type']}")
            # print(f"Description: {details['description']}")
            # print(f"Default: {details['default']}")
            # Constraints might not always have values, so check if it's not empty before printing
            if details['constraints']:
                # print("Constraints:")
                for constraint, value in details['constraints'].items():
                    pass
                    # print(f"  {constraint}: {value}")
            # print("-" * 40)  # Separator for readability

    def format_data(self, data):

        formatted_data = data

        return formatted_data
