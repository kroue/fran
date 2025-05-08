import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom"; // Import useNavigate
import Banner from "../../components/Banner/Banner";
import BannerBottom from "../../components/Banner/BannerBottom";
import BestSellers from "../../components/home/BestSellers/BestSellers";
import NewArrivals from "../../components/home/NewArrivals/NewArrivals";
import Sale from "../../components/home/Sale/Sale";
import SpecialOffers from "../../components/home/SpecialOffers/SpecialOffers";
import YearProduct from "../../components/home/YearProduct/YearProduct";

const Home = () => {
  const [user, setUser] = useState(null);
  const navigate = useNavigate(); // Initialize useNavigate

  useEffect(() => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      setUser(JSON.parse(storedUser)); // Parse and set user data
    }
  }, []);

  const handleLogout = () => {
    localStorage.removeItem("user"); // Remove user data from localStorage
    localStorage.removeItem("token"); // Remove token if stored
    setUser(null); // Reset user state
    navigate("/signin"); // Redirect to the sign-in page
  };

  const handleAdminRedirect = () => {
    navigate("/admin"); // Redirect to the admin page
  };

  return (
    <div className="w-full mx-auto">
      {user && (
        <div className="welcome-message text-center py-4 bg-gray-100">
          <h1 className="text-xl font-bold">Welcome, {user.username}!</h1>
          <button
            onClick={handleLogout}
            className="mt-4 px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600"
          >
            Logout
          </button>
          <button
            onClick={handleAdminRedirect}
            className="mt-4 ml-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Admin Panel
          </button>
        </div>
      )}
      <Banner />
      <BannerBottom />
      <div className="max-w-container mx-auto px-4">
        <Sale />
        <NewArrivals />
        <BestSellers />
        <YearProduct />
        <SpecialOffers />
      </div>
    </div>
  );
};

export default Home;