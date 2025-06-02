'use client';

interface BrandCardProps {
    brand: {
        company_name?: string,
        website_url?: string,
        target_audience?: string,
        title?: string,
        description?: string,
        og_title?: string,
        og_description?: string,
        writing_style?: string,
        brand_colors?: string[],
        [key: string]: any
    }
}

export default function BrandCard({brand}: BrandCardProps) {
    return (
        <div className="text-black w-120">
            <h2 className="font-bold text-lg text-center mt-12 mb-4">Brand Information</h2>
            <h3 className="font-semibold text-sm mt-2">Company Name</h3>
            <p className="mt-2" >{brand.company_name}</p>
            <h3 className="font-semibold text-sm mt-2">Website URL</h3>
            <p className="mt-2">{brand.website_url}</p>
            <h3 className="font-semibold text-sm mt-2">Target Audience</h3>
            <p className="mt-2">{brand.target_audience}</p>
            <h3 className="font-semibold text-sm mt-2">Writing Style</h3>
            <p className="mt-2">{brand.writing_style}</p>
            <h3 className="font-semibold text-sm mt-2">Title</h3>
            <p className="mt-2">{brand.title}</p>
            <h3 className="font-semibold text-sm mt-2">Description</h3>
            <p className="mt-2">{brand.description}</p>
            <h3 className="font-semibold text-sm mt-2">OG Title</h3>
            <p className="mt-2">{brand.og_title}</p>
            <h3 className="font-semibold text-sm mt-2">OG Description</h3>
            <p className="mt-2">{brand.og_description}</p>
            <h3 className="font-semibold text-sm mt-2">Brand Colors</h3>
            <p className="mt-2">{brand.brand_colors?.map((color: string) => color).join(", ")}</p>
        </div>
    )
}
