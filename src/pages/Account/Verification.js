import React, { useState } from "react"; // Import useState
import { useLocation, useNavigate } from "react-router-dom"; // Import useLocation and useNavigate
import axios from "axios"; // Import axios

const VerifyEmail = () => {
  const [code, setCode] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");
  const location = useLocation();
  const navigate = useNavigate();

  // Retrieve the email passed from the signup page
  const email = location.state?.email;

  const handleVerify = async () => {
    if (!email) {
      setError("Email is missing. Please try signing up again.");
      return;
    }

    try {
      await axios.post("http://127.0.0.1:8000/api/accounts/verify-code/", {
        email,
        code,
      });
      setSuccess("Account verified successfully!");
      setError("");
      setTimeout(() => navigate("/signin"), 2000); // Redirect to sign-in page after 2 seconds
    } catch (error) {
      console.error("Error Response:", error.response?.data || error.message);
      setError(error.response?.data?.error || "Invalid verification code. Please try again.");
      setSuccess("");
    }
  };

  return (
    <div className="w-full h-screen flex items-center justify-center">
      <div className="w-[400px] p-6 bg-white shadow-md rounded">
        <h1 className="text-xl font-bold mb-4">Verify Your Account</h1>
        <p className="text-sm text-gray-600 mb-4">
          Enter the verification code sent to your email: <strong>{email}</strong>
        </p>
        <input
          type="text"
          placeholder="Enter verification code"
          value={code}
          onChange={(e) => setCode(e.target.value)}
          className="w-full mb-4 p-2 border rounded"
        />
        {error && <p className="text-red-500 text-sm mb-2">{error}</p>}
        {success && <p className="text-green-500 text-sm mb-2">{success}</p>}
        <button
          onClick={handleVerify}
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600"
        >
          Verify
        </button>
      </div>
    </div>
  );
};

export default VerifyEmail;