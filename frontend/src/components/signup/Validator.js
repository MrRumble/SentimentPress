class Validator {

    static validateEmail(email) {
        // Regular expression for email validation
        const emailRegex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

        // Test the email against the regex
        return emailRegex.test(String(email).toLowerCase());
    }

    static validatePassword(password) {
        // Initialize an object to store validation results
        const result = {
            isValid: true,
            errors: []
        };

        // Check length
        if (password.length < 8) {
            result.isValid = false;
            result.errors.push("Password must be 8 characters or longer");
        }

        // Check for lowercase letter
        if (!/[a-z]/.test(password)) {
            result.isValid = false;
            result.errors.push("Password must include at least one lowercase letter");
        }

        // Check for uppercase letter
        if (!/[A-Z]/.test(password)) {
            result.isValid = false;
            result.errors.push("Password must include at least one uppercase letter");
        }

        // Check for number
        if (!/\d/.test(password)) {
            result.isValid = false;
            result.errors.push("Password must include at least one number");
        }

        // Check for special character
        if (!/[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)) {
            result.isValid = false;
            result.errors.push("Password must include at least one special character");
        }

        return result;
    }
}


export default Validator;