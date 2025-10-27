import React, { useState, useEffect } from "react";
import { Product } from "@/entities/Product";
import ProductFilters from "../components/products/ProductFilters";
import ProductGrid from "../components/products/ProductGrid";
import { Grid, List } from "lucide-react";

export default function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchTerm, setSearchTerm] = useState("");
  const [showFilters, setShowFilters] = useState(false);
  const [viewMode, setViewMode] = useState("grid");
  
  const [filters, setFilters] = useState({
    category: 'all',
    sizes: [],
    colors: [],
    priceRange: { min: '', max: '' }
  });

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    setLoading(true);
    try {
      const allProducts = await Product.list('-created_date');
      setProducts(allProducts);
    } catch (error) {
      console.error("Error loading products:", error);
    } finally {
      setLoading(false);
    }
  };

  const filteredProducts = products.filter(product => {
    // Search filter
    const matchesSearch = !searchTerm || 
      product.name.toLowerCase().includes(searchTerm.toLowerCase()) ||
      product.description.toLowerCase().includes(searchTerm.toLowerCase());

    // Category filter
    const matchesCategory = filters.category === 'all' || product.category === filters.category;

    // Size filter
    const matchesSize = filters.sizes.length === 0 || 
      filters.sizes.some(size => product.sizes?.includes(size));

    // Color filter
    const matchesColor = filters.colors.length === 0 || 
      filters.colors.some(color => product.colors?.includes(color));

    // Price filter
    const matchesPrice = (!filters.priceRange.min || product.price >= parseFloat(filters.priceRange.min)) &&
      (!filters.priceRange.max || product.price <= parseFloat(filters.priceRange.max));

    return matchesSearch && matchesCategory && matchesSize && matchesColor && matchesPrice;
  });

  return (
    <div className="min-h-screen py-8">
      <div className="max-w-7xl mx-auto px-6">
        {/* Page Header */}
        <div className="neumorphic rounded-2xl p-6 mb-8">
          <div className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
            <div>
              <h1 className="text-3xl font-bold text-gray-800 mb-2">Our Collection</h1>
              <p className="text-gray-600">
                Discover our carefully curated selection of premium clothing
              </p>
            </div>
            
            {/* View Toggle */}
            <div className="flex items-center gap-2">
              <span className="text-sm text-gray-600">
                {loading ? 'Loading...' : `${filteredProducts.length} products`}
              </span>
              <div className="ml-4 neumorphic-inset rounded-lg p-1 flex">
                <button
                  onClick={() => setViewMode('grid')}
                  className={`p-2 rounded-md transition-all duration-200 ${
                    viewMode === 'grid' 
                      ? 'neumorphic' 
                      : 'hover:shadow-[-1px_-1px_2px_rgba(255,255,255,0.8),1px_1px_2px_rgba(0,0,0,0.1)]'
                  }`}
                >
                  <Grid className="w-4 h-4 text-gray-600" />
                </button>
                <button
                  onClick={() => setViewMode('list')}
                  className={`p-2 rounded-md transition-all duration-200 ${
                    viewMode === 'list' 
                      ? 'neumorphic' 
                      : 'hover:shadow-[-1px_-1px_2px_rgba(255,255,255,0.8),1px_1px_2px_rgba(0,0,0,0.1)]'
                  }`}
                >
                  <List className="w-4 h-4 text-gray-600" />
                </button>
              </div>
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-4 gap-8">
          {/* Filters Sidebar */}
          <div className="lg:col-span-1">
            <ProductFilters
              filters={filters}
              onFiltersChange={setFilters}
              searchTerm={searchTerm}
              onSearchChange={setSearchTerm}
              showFilters={showFilters}
              onToggleFilters={() => setShowFilters(!showFilters)}
            />
          </div>

          {/* Products Grid */}
          <div className="lg:col-span-3">
            <div className="neumorphic rounded-2xl p-6">
              <ProductGrid products={filteredProducts} loading={loading} />
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}