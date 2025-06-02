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
        <div>
            <h2 className="font-bold text-lg">Brand Information</h2>
            <p className="mt-2" >{brand.company_name}</p>
            <p className="mt-2">{brand.website_url}</p>
            <p className="mt-2">{brand.target_audience}</p>
            <p className="mt-2">{brand.writing_style}</p>
            <p className="mt-2">{brand.title}</p>
            <p className="mt-2">{brand.description}</p>
            <p className="mt-2">{brand.og_title}</p>
            <p className="mt-2">{brand.og_description}</p>
            <p className="mt-2">{brand.brand_colors?.map((color: string) => color).join(", ")}</p>
        </div>
    )
}
